---
기술지원명: What if I'm rate-limited?
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: What if I'm rate-limited?
출처링크: https://help.figma.com/hc/en-us/articles/34963238552855-What-if-I-m-rate-limited
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

When you're using third-party integrations and apps, you may occasionally get a message that you've been rate-limited.

This happens because apps and integrations are only allowed to make a certain number of requests to our REST API on your behalf. The limit depends on your plan, seat, and the location of the file.

For example, if the integration or app tries to get the content of a file in a Starter plan for you, requests to that file are limited to up to 6 per month even if you have a Full seat in a different plan.

Depending on your plan and seat, [upgrading can increase the limit](https://help.figma.com/hc/en-us/articles/360046216313).

If a file you're trying to work with is being rate-limited and you have already have a Full seat in a paid plan, check if the file is in a Starter plan. If it is, try [saving a local copy](https://help.figma.com/hc/en-us/articles/8403626871063) of the file and [importing it](https://help.figma.com/hc/en-us/articles/360041003114) to your paid plan. Once moved, higher rate limits should be applied.

For more assistance, you should reach out directly to the creator of the app or integration. The listing for an app in the Figma Community includes a support website or contact you can reach out to.

## Rate limits

Rate limits are applied based on your plan, seat, and where the resource you're trying to access resides. The following table lists the rate limits.

| API tier | Seat | Starter | Professional | Organization | Enterprise |
| --- | --- | --- | --- | --- | --- |
| Tier 1 | View, Collab | Up to 6/month | Up to 6/month | Up to 6/month | Up to 6/month |
| Dev, Full | 10/min | 15/min | 20/min |
| Tier 2 | View, Collab | Up to 5/min | Up to 5/min | Up to 5/min | Up to 5/min |
| Dev, Full | 25/min | 50/min | 100/min |
| Tier 3 | View, Collab | Up to 10/min | Up to 10/min | Up to 10/min | Up to 10/min |
| Dev, Full | 50/min | 100/min | 150/min |

The API tier is determined by the endpoint. For example, getting content or images from a file is Tier 1, whereas requesting library analytics is Tier 3.

**Note:** If you're the developer of an app or integration that's being rate-limited, see our [developer documentation](https://developers.figma.com/docs/rest-api/rate-limits/).
