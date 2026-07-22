"""PR 머지 시 (승인 대기) 필드를 실제 값으로 채운다.

- 승인자: PR의 마지막 APPROVED 리뷰어 (없으면 머지한 사람)
- 게시일: 머지일
- 검토일: 게시일과 동일하게 초기화
GitHub Actions에서 호출: python scripts/fill_approval.py <PR번호>
필요 환경변수: GITHUB_TOKEN, GITHUB_REPOSITORY
"""
import json
import os
import re
import subprocess
import sys
from datetime import date


def gh_api(path: str) -> list | dict:
    out = subprocess.check_output(["gh", "api", path])
    return json.loads(out)


def main() -> None:
    pr = sys.argv[1]
    repo = os.environ["GITHUB_REPOSITORY"]

    reviews = gh_api(f"repos/{repo}/pulls/{pr}/reviews")
    approver = next((r["user"]["login"] for r in reversed(reviews)
                     if r["state"] == "APPROVED"), None)
    if not approver:
        pr_data = gh_api(f"repos/{repo}/pulls/{pr}")
        approver = (pr_data.get("merged_by") or {}).get("login", "unknown")

    files = gh_api(f"repos/{repo}/pulls/{pr}/files?per_page=100")
    today = date.today().isoformat()
    changed = []
    for f in files:
        path = f["filename"]
        if not path.endswith(".md") or f["status"] == "removed":
            continue
        if not (path.startswith("figma-help/") or path.startswith("mail-threads/")):
            continue
        try:
            with open(path, encoding="utf-8") as fp:
                text = fp.read()
        except FileNotFoundError:
            continue
        new = text.replace("승인자: (승인 대기)", f"승인자: {approver}")
        new = new.replace("게시일: (승인 대기)", f"게시일: {today}")
        new = new.replace("검토일: (승인 대기)", f"검토일: {today}")
        if new != text:
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(new)
            changed.append(path)

    print(json.dumps({"approver": approver, "date": today, "files": changed},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
