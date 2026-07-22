"""공통 유틸: Claude API 호출, 마크다운 생성, 슬러그."""
import os
import re
import json
import urllib.request

CATEGORIES = ["디자인", "보안", "개발", "API", "관리", "계약"]
ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-sonnet-4-6"


def claude(prompt: str, max_tokens: int = 4000) -> str:
    """Claude API 단일 호출. ANTHROPIC_API_KEY 환경변수 필요."""
    api_key = os.environ["ANTHROPIC_API_KEY"]
    body = json.dumps({
        "model": MODEL,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()
    req = urllib.request.Request(
        ANTHROPIC_API_URL,
        data=body,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
    return "".join(b.get("text", "") for b in data["content"] if b["type"] == "text").strip()


def extract_json(text: str) -> dict:
    """Claude 응답에서 JSON 오브젝트 추출 (코드펜스 제거 포함)."""
    cleaned = re.sub(r"```(json)?", "", text).strip()
    start, end = cleaned.find("{"), cleaned.rfind("}")
    return json.loads(cleaned[start:end + 1])


def slugify(text: str, max_len: int = 60) -> str:
    s = re.sub(r"[^\w가-힣-]+", "-", text.strip()).strip("-")
    return s[:max_len].rstrip("-") or "untitled"


def build_markdown(fields: dict, body: str) -> str:
    """규약(guidelines/TEMPLATE.md)에 맞는 문서 생성."""
    category = fields["카테고리"]
    if category not in CATEGORIES:
        category = "관리"  # 예외 없음 — 분류 실패 시 관리로 강제
    lines = [
        "---",
        f"기술지원명: {fields['기술지원명']}",
        f"카테고리: {category}",
        f"작성자: {fields['작성자']}",
        "승인자: (승인 대기)",
        f"출처: {fields['출처']}",
    ]
    if fields.get("출처링크"):
        lines.append(f"출처링크: {fields['출처링크']}")
    lines += [
        "게시일: (승인 대기)",
        "검토일: (승인 대기)",
        "---",
        "",
        body.strip(),
        "",
    ]
    return "\n".join(lines)


def load_state(path: str) -> dict:
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_state(path: str, state: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2, sort_keys=True)
