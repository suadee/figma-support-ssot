"""Outlook 메일 인제스트 (Microsoft Graph API).

support+tangunsoft@figma.com, support@figma.com 과 주고받은 메일을
대화(conversation) 단위로 묶어 규약에 맞는 md로 변환한다.

인증: Azure 앱 등록(무료) 후 Device Code Flow — 처음 실행 시 브라우저에서
      코드 입력으로 로그인. 토큰 캐시(state/.msal_cache)로 이후 자동 갱신.
사용: ANTHROPIC_API_KEY=... GRAPH_CLIENT_ID=... python scripts/ingest_outlook.py [--days 90]
의존: pip install msal requests
"""
import argparse
import html
import json
import re
import sys
from datetime import datetime, timedelta, timezone

import msal
import requests

from common import claude, extract_json, slugify, build_markdown, load_state, save_state, CATEGORIES

SUPPORT_ADDRESSES = ["support+tangunsoft@figma.com", "support@figma.com"]
GRAPH = "https://graph.microsoft.com/v1.0"
SCOPES = ["Mail.Read"]
MANIFEST = "state/outlook_manifest.json"
CACHE = "state/.msal_cache"
OUT_DIR = "mail-threads"


def get_token(client_id: str) -> str:
    cache = msal.SerializableTokenCache()
    try:
        with open(CACHE) as f:
            cache.deserialize(f.read())
    except FileNotFoundError:
        pass
    app = msal.PublicClientApplication(
        client_id, authority="https://login.microsoftonline.com/common", token_cache=cache)
    result = None
    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
    if not result:
        flow = app.initiate_device_flow(scopes=SCOPES)
        print(flow["message"], file=sys.stderr)  # 브라우저에서 코드 입력 안내
        result = app.acquire_token_by_device_flow(flow)
    if "access_token" not in result:
        raise SystemExit(f"인증 실패: {result.get('error_description')}")
    with open(CACHE, "w") as f:
        f.write(cache.serialize())
    return result["access_token"]


def fetch_messages(token: str, since: datetime) -> list[dict]:
    """지원 주소와 주고받은 메일 수집 ($search 사용, participants 기준)."""
    headers = {"Authorization": f"Bearer {token}", "ConsistencyLevel": "eventual"}
    seen, out = set(), []
    for addr in SUPPORT_ADDRESSES:
        url = (f"{GRAPH}/me/messages?$search=\"participants:{addr}\""
               f"&$select=id,conversationId,subject,from,toRecipients,receivedDateTime,body"
               f"&$top=50")
        while url:
            r = requests.get(url, headers=headers, timeout=60)
            r.raise_for_status()
            data = r.json()
            for m in data.get("value", []):
                if m["id"] in seen:
                    continue
                seen.add(m["id"])
                if datetime.fromisoformat(m["receivedDateTime"].replace("Z", "+00:00")) >= since:
                    out.append(m)
            url = data.get("@odata.nextLink")
    return out


def html_to_text(raw: str) -> str:
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", raw or "", flags=re.S)
    text = re.sub(r"<br\s*/?>|</p>|</div>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(re.sub(r"\n{3,}", "\n\n", text)).strip()


def tangunsoft_author(messages: list[dict]) -> str:
    """스레드에서 단군소프트 측 참여자(작성자) 추출."""
    for m in messages:
        addr = m.get("from", {}).get("emailAddress", {})
        email = (addr.get("address") or "").lower()
        if email and "figma.com" not in email:
            return addr.get("name") or email
    return "단군소프트"


def convert(thread: list[dict]) -> str:
    thread.sort(key=lambda m: m["receivedDateTime"])
    subject = thread[0].get("subject") or "(제목 없음)"
    author = tangunsoft_author(thread)
    convo = "\n\n---\n\n".join(
        f"[{m['receivedDateTime'][:10]}] {m['from']['emailAddress'].get('name', '')} "
        f"<{m['from']['emailAddress'].get('address', '')}>\n"
        f"{html_to_text(m['body'].get('content', ''))[:6000]}"
        for m in thread)[:20000]

    prompt = f"""너는 단군소프트의 Figma 기술지원 SSoT 문서 작성기다.
아래 Figma 지원팀과의 메일 스레드를 기술지원 문서로 변환하라.

메일 제목: {subject}
스레드:
{convo}

규칙:
- 고객사명·개인 이름·이메일·전화번호·금액은 반드시 마스킹 (예: "고객사 A", "담당자")
- 단군소프트 담당자와 Figma 지원팀 이름은 마스킹하지 않아도 됨
- 재사용 가능한 답변 초안을 반드시 포함

JSON으로만 응답하라 (코드펜스 없이):
{{
  "기술지원명": "<전체 내용 한 줄 요약 제목>",
  "카테고리": "<{'|'.join(CATEGORIES)} 중 반드시 하나>",
  "내용": "<## 내용 아래 마크다운. 문의 배경 → Figma 답변 요지 → 결론>",
  "메일초안": "<유사 문의에 재사용할 한국어 답변 초안>"
}}"""
    parsed = extract_json(claude(prompt))
    fields = {
        "기술지원명": parsed["기술지원명"],
        "카테고리": parsed["카테고리"],
        "작성자": author,
        "출처": subject,
    }
    body = f"## 내용\n\n{parsed['내용']}\n\n## 메일 초안\n\n{parsed['메일초안']}"
    return build_markdown(fields, body)


def main() -> None:
    import os
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=90, help="수집 기간 (기본 90일)")
    args = ap.parse_args()

    token = get_token(os.environ["GRAPH_CLIENT_ID"])
    since = datetime.now(timezone.utc) - timedelta(days=args.days)
    messages = fetch_messages(token, since)

    threads: dict[str, list[dict]] = {}
    for m in messages:
        threads.setdefault(m["conversationId"], []).append(m)

    manifest = load_state(MANIFEST)
    processed = 0
    for cid, msgs in threads.items():
        latest = max(m["receivedDateTime"] for m in msgs)
        if manifest.get(cid, {}).get("latest") == latest:
            continue  # 변화 없는 스레드 스킵
        try:
            md = convert(msgs)
        except Exception as e:
            print(f"  실패 {cid}: {e}", file=sys.stderr)
            continue
        subject = msgs[0].get("subject") or "untitled"
        path = f"{OUT_DIR}/{latest[:10]}-{slugify(subject)}.md"
        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
        manifest[cid] = {"subject": subject, "latest": latest, "file": path,
                         "messages": len(msgs)}
        processed += 1
        print(f"  저장 {path}", file=sys.stderr)

    save_state(MANIFEST, manifest)
    print(json.dumps({"threads": len(threads), "processed": processed}, ensure_ascii=False))


if __name__ == "__main__":
    main()
