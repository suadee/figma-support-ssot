"""Figma 헬프센터(Zendesk) 인제스트 — LLM/API 키 불필요 버전.

1) sections API로 섹션→카테고리 매핑 구성 (scripts/category_map.json 규칙)
2) articles API로 전체 문서 목록 수집 → state/figma_manifest.json 과 diff
3) 신규·변경 문서 본문을 markdownify로 기계 변환 → figma-help/ 저장
4) manifest 갱신. PR 생성은 GitHub Actions가 담당.

사용: python scripts/ingest_figma_help.py [--limit N] [--category-ids 1,2]
의존: pip install markdownify
"""
import argparse
import json
import re
import sys
import time
import urllib.request

from markdownify import markdownify

from common import slugify, build_markdown, load_state, save_state

HC = "https://help.figma.com/api/v2/help_center/en-us"
MANIFEST = "state/figma_manifest.json"
MAP_FILE = "scripts/category_map.json"
OUT_DIR = "figma-help"


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "tangunsoft-ssot-bot"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())


def fetch_all(endpoint: str, key: str) -> list[dict]:
    items, url = [], f"{HC}/{endpoint}.json?per_page=100"
    while url:
        data = fetch_json(url)
        items.extend(data.get(key, []))
        url = data.get("next_page")
        time.sleep(0.4)
    return items


def build_category_resolver() -> callable:
    with open(MAP_FILE, encoding="utf-8") as f:
        cfg = json.load(f)
    sections = {str(s["id"]): s for s in fetch_all("sections", "sections")}

    def resolve(section_id) -> str:
        sec = sections.get(str(section_id))
        if not sec:
            return cfg["default"]
        name = sec["name"].lower()
        for rule in cfg["keyword_rules"]:
            if any(kw in name for kw in rule["keywords"]):
                return rule["category"]
        return cfg["zendesk_category_map"].get(str(sec["category_id"]), cfg["default"])

    return resolve, sections


def convert(article: dict, category: str) -> str:
    body_md = markdownify(article.get("body") or "", heading_style="ATX", bullets="-")
    body_md = re.sub(r"\n{3,}", "\n\n", body_md).strip()
    fields = {
        "기술지원명": article["title"],
        "카테고리": category,
        "작성자": "Figma",
        "출처": article["title"],
        "출처링크": article["html_url"],
    }
    return build_markdown(fields, "## 내용\n\n" + body_md)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="처리 문서 수 상한 (0=무제한)")
    ap.add_argument("--category-ids", default="", help="특정 Zendesk 카테고리만 (쉼표 구분)")
    args = ap.parse_args()

    resolve, sections = build_category_resolver()
    manifest = load_state(MANIFEST)
    articles = fetch_all("articles", "articles")

    if args.category_ids:
        wanted = set(args.category_ids.split(","))
        articles = [a for a in articles
                    if str(sections.get(str(a.get("section_id")), {}).get("category_id")) in wanted]

    current_ids = {str(a["id"]) for a in articles}
    new = [a for a in articles if str(a["id"]) not in manifest]
    changed = [a for a in articles if str(a["id"]) in manifest
               and manifest[str(a["id"])].get("updated_at") != a["updated_at"]]
    deleted = sorted(set(k for k in manifest if not manifest[k].get("deleted")) - current_ids)

    todo = sorted(new + changed, key=lambda a: a["updated_at"], reverse=True)
    if args.limit:
        todo = todo[:args.limit]
    print(f"전체 {len(articles)} / 신규 {len(new)} / 변경 {len(changed)}"
          f" / 삭제 감지 {len(deleted)} / 이번 처리 {len(todo)}", file=sys.stderr)

    for a in todo:
        aid = str(a["id"])
        old_file = manifest.get(aid, {}).get("file")
        path = old_file or f"{OUT_DIR}/{aid}-{slugify(a['title'])}.md"
        try:
            md = convert(a, resolve(a.get("section_id")))
        except Exception as e:
            print(f"  실패 {aid} {a['title']}: {e}", file=sys.stderr)
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
        manifest[aid] = {"title": a["title"], "url": a["html_url"],
                         "updated_at": a["updated_at"], "file": path}
        print(f"  저장 {path}", file=sys.stderr)

    for aid in deleted:
        manifest[aid]["deleted"] = True  # 파일 삭제는 PR에서 사람이 판단

    save_state(MANIFEST, manifest)
    print(json.dumps({"new": len(new), "changed": len(changed), "deleted": deleted},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
