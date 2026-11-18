---
name: whatsapp-template
description: Write a WhatsApp marketing message template for SmartyTap in Chargezen — header, message with variables, footer, link and opt-out buttons — submit it to Meta for review on the merchant's OK, check Meta's answer, fix and resubmit a rejected one, and use an approved one in a campaign or flow. Use when they want to send WhatsApp marketing, ask why a template was rejected, or check which templates are approved.
argument-hint: "<what the message is for> [language]"
---

# WhatsApp template

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

WhatsApp marketing goes out only as a template Meta approved. SmartyTap always submits templates as Marketing, from the workspace's connected WhatsApp number; connecting the number is done in SmartyTap. Campaigns and flows send them only to people who joined on WhatsApp, never to US numbers, between 8am and 8pm their time. Meta bills the merchant's WhatsApp account for each message; it uses no SMS credit.

## 1. Check what's there

`smartytap_whatsapp_templates.list` with Meta's status for each. If one already says what they want, offer it. For a rejected or paused one, read it with `smartytap_whatsapp_templates.get`: `status_note` says why, and `problems` says what stops a review.

## 2. Write it

- **Name** (team only) and **language** in Meta's code, such as `en_US` or `es_ES`.
- **Header:** optional short line; at most one variable `{{1}}`, with an example.
- **Message:** short and specific, variables numbered `{{1}}`, `{{2}}` without gaps, each with an example value for Meta's reviewers (a first name, a product).
- **Footer:** optional, no variables.
- **Buttons:** at most two links (`https://`, which may end in one `{{1}}` with an example), quick replies, and always an **opt-out** button so people can stop promotions.

Meta rejects vague, misleading or all-variable messages. Write the offer in words, and only promise what the store really offers. Show the person the template exactly as it'll be submitted.

## 3. Submit and follow up

1. On their OK: `smartytap_whatsapp_templates.create` with a new `operation_id`. It goes to Meta right away; review can take up to 24 hours.
2. Check later with `smartytap_whatsapp_templates.get`: `approved`, or `rejected` with Meta's reason.
3. **Fix a rejection:** change what the reason names and resubmit with `smartytap_whatsapp_templates.update`, passing the `version` you read. Editing a version Meta has seen makes a new version; campaigns and flows keep sending the earlier approved version until Meta approves the new one. A name-only change isn't reviewed.

## 4. Use it

Once approved: a campaign's WhatsApp message (`/campaign`, with the template's id) or a flow's **WhatsApp message** step. Campaign review and flow activation both check Meta's approval; a template Meta later pauses or turns off stops sending, so check it again before a big send.
