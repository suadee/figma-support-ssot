---
기술지원명: View your sales metrics
카테고리: 관리
작성자: Figma
승인자: (승인 대기)
출처: View your sales metrics
출처링크: https://help.figma.com/hc/en-us/articles/12818240767255-View-your-sales-metrics
게시일: (승인 대기)
검토일: (승인 대기)
---

## 내용

Before you Start

Who can use this feature

 

Users who have been approved to sell resources on Community

After you have been approved to sell on the Community, the **Metrics** tab becomes available on your Community profile. The information on this tab is only visible to you.

As you sell resources, the **Metrics** tab displays:

- The total number of views your paid resources have received
- Your total number of purchases. This number includes one-time payments and recurring monthly subscriptions multiplied by the number of subscribers
- Your total amount earned from all purchases

In addition to your total overall metrics, you can see these metrics broken down by each resource.

![Metrics tab showing total views, purchases, and earnings for a seller's resources, with a button to view Stripe dashboard.](https://help.figma.com/hc/article_attachments/12818238041367)

Once you start selling resources, you can click **View payout statements** to download a CSV file that contains all activity within your payment account. Payout statements are generated on the 2nd of each month for the previous month. The following table explains each column included in the CSV file:

|  |  |
| --- | --- |
| **Column** | **Description** |
| TRANSACTION\_DATE (UTC) | The date the transaction occurred in Coordinated Universal Time (UTC) |
| DESCRIPTION | Description of the charge |
| NET\_PAY (USD) | The amount that the creator earned from the transaction in USD |
| NET\_PAY\_IN\_CREATOR\_CURRENCY | The amount that the creator earned from the transaction in their local currency |
| CREATOR\_CURRENCY | The creator's local currency |
| INVOICE\_ID | The invoice id |
| INVOICE\_SUBTOTAL (USD) | The subtotal of the invoice in USD |
| INVOICE\_TAX\_RATE | The tax rate charged on the invoice |
| INVOICE\_TAX (USD) | The taxed amount charged on the invoice in USD |
| INVOICE\_TOTAL (USD) | The total amount invoiced in USD |
| CUSTOMER\_COUNTRY | The country where the customer resides |
| CUSTOMER\_REGION | The region where the customer resides (if applicable) |
| FILE\_ID | The id of the sold file (if applicable) |
| PLUGIN\_ID | The id of the sold plugin (if applicable) |
| WIDGET\_ID | The id of the sold widget (if applicable) |
| FIGMA\_COMMISSION (USD) | The fee amount Figma collects from the transaction |

You can also access a more in-depth look at these metrics from your Stripe dashboard. Click View Stripe dashboard to be redirected to Stripe. For more information, see [Dashboard basics](https://stripe.com/docs/dashboard/basics) from Stripe’s help documentation.

Note: **Why are my total earnings different?** You may notice that the total earnings number differs when viewed from the **Metrics** tab vs your Stripe dashboard. That is because the **Metrics** tab displays your gross total and Stripe displays your actual payout total after fees have been deducted.
