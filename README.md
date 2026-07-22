# Figma 기술지원 SSoT

단군소프트 기술지원 단일 진실 공급원. Outlook 지원 메일 + Figma 헬프센터를 수집·가공해 마크다운으로 축적하고, 챗봇과 Obsidian이 이를 소비한다. **API 키 없이 운영된다.**

## 구조

```
figma-help/      Figma 헬프센터 문서 (작성자: Figma) — 무LLM 기계 변환
mail-threads/    Figma 지원 메일 스레드 문서 — Claude 정기 작업이 생성
guidelines/      문서 형식 규약 (TEMPLATE.md)
scripts/         인제스트·운영 스크립트 (category_map.json = 카테고리 매핑 규칙)
state/           manifest (diff 기준점) — 커밋 대상
```

## 플로우

인풋(Outlook / Figma 헬프) → 가공 → **PR** → 사람 승인 → main 반영 → 챗봇·Obsidian 소비

- 승인자·게시일·검토일: PR 머지 시 자동 기입 (`on-merge-fill-approval.yml`)
- 검토일 90일 초과 문서: 매월 1일 이슈로 리스트업 (`monthly-stale-check.yml`)

## 레인별 동작

### 1) Figma 헬프센터 — 완전 자동, 완전 무료
- 매주 월요일 09:00 KST `figma-help-sync` 워크플로가 실행 (LLM 미사용)
- Zendesk API로 목록 수집 → manifest diff → 신규/변경분만 markdownify로 원문 변환
- 카테고리는 `scripts/category_map.json`의 섹션 키워드 규칙 + Zendesk 카테고리 매핑으로 결정
  (보안: SSO/SAML/SCIM/security 섹션, 계약: billing/plan/seats, API: api/webhook/mcp, 개발: dev mode/plugin/code)
- 초기 백필: Actions 탭에서 수동 실행, limit=0 (전체 약 870건, 무료)

### 2) Outlook 메일 — Claude 정기 작업 (구독 내)
Claude 스케줄 작업이 매주 실행: M365 커넥터로 support+tangunsoft@figma.com,
support@figma.com 스레드 확인 → 규약(guidelines/TEMPLATE.md)에 맞게 md 가공
(고객 정보 마스킹) → GitHub 커넥터로 PR 생성.

대안: `scripts/ingest_outlook.py` (로컬 실행, 단 Claude API 키 필요 — 기본 경로 아님)

## 셋업 (1회)

1. 이 레포를 GitHub에 push (프라이빗 필수 — 메일 문서에 고객 맥락 포함)
2. Actions 탭에서 `figma-help-sync` 수동 실행 (limit=0)으로 초기 백필 → PR 검토·머지
3. Claude에서 메일 정기 작업 등록 (프롬프트는 팀 위키/작업 설정 참고)

## 운영 원칙

- 자동화 레인은 **PR 필수**, 큐레이터의 Obsidian/Claude Code 직접 편집은 main 커밋 허용
- 메일 문서의 고객 정보는 가공 단계에서 마스킹 — PR 리뷰 시 재확인
- 삭제 감지된 헬프 문서는 자동 삭제하지 않음 (manifest에 deleted 표시, 사람이 판단)
- 카테고리 오분류 발견 시 `scripts/category_map.json` 규칙을 수정 (코드 수정 불필요)
