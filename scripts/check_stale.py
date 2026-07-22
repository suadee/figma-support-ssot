"""검토일이 90일을 초과한 문서를 리스트업한다 (매월 이슈 생성용)."""
import glob
import re
import sys
from datetime import date, timedelta

THRESHOLD = timedelta(days=90)


def main() -> None:
    stale = []
    for path in glob.glob("figma-help/*.md") + glob.glob("mail-threads/*.md"):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        m = re.search(r"^검토일: (\d{4}-\d{2}-\d{2})", text, re.M)
        if not m:
            stale.append((path, "검토일 없음"))
            continue
        reviewed = date.fromisoformat(m.group(1))
        if date.today() - reviewed > THRESHOLD:
            stale.append((path, m.group(1)))

    if not stale:
        print("검토 기한 초과 문서 없음")
        return
    print(f"## 검토일 90일 초과 문서 ({len(stale)}건)\n")
    for path, reviewed in sorted(stale, key=lambda x: x[1]):
        print(f"- [ ] `{path}` — 최종 검토: {reviewed}")
    sys.exit(0)


if __name__ == "__main__":
    main()
