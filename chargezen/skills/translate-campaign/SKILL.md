---
name: translate-campaign
description: Add a translated version of a SmartyTap campaign email, text or WhatsApp message in Chargezen, sent only to people whose profile language matches while everyone else gets the original — written in that language, previewed and counted before it launches. Use when they want a campaign in Spanish, French or another language, or to reach customers in their own language.
argument-hint: "<campaign> <language>"
---

# Translate a campaign

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Find the campaign and message

`chargezen.smartytap_campaigns.list.v1`, then `chargezen.smartytap_campaigns.get.v1`. Translation works on a draft message that isn't scheduled yet, and only on an original (a translation can't be translated again). If the campaign is already scheduled, it has to be unscheduled first (`/manage-campaign`); say so.

Each message goes only to people whose **profile language** is the one chosen; people with no language set, or another one, get the original. If few people have that language on their profile, the translation will reach few: `chargezen.smartytap_campaigns.preview_audience.v1` in step 3 shows how many.

## 2. Add and write it

1. `chargezen.smartytap_campaigns.translate_message.v1` with the message id and the language as a lowercase code (`es`, `fr`, `de`). It starts as a copy of the original with no send time. Asking again for the same language returns the one already there.
2. Write it in that language yourself, keeping the same offer, link and meaning:
   - **Email:** `chargezen.email_documents.get.v1` then `chargezen.email_documents.apply_ops.v1` at the new message's document address: subject, preview text and every text block. Keep personalization tokens exactly as they are.
   - **Text:** the body and its send time in the campaign definition with `chargezen.smartytap_campaigns.update.v2` (read the revision first). Mind length: accented characters can make a text cost more parts.
   - **WhatsApp:** it needs a template approved in that language (`/whatsapp-template`).
3. Give it the same send time as the original unless they want otherwise.

Write naturally, the way a native speaker in that market would, not word for word. Offer to have a native speaker on their team check it with `chargezen.smartytap_campaigns.send_test.v2`.

## 3. Check and launch

- `chargezen.smartytap_campaigns.review.v1`, then `chargezen.smartytap_campaigns.preview.v2` for each version.
- `chargezen.smartytap_campaigns.preview_audience.v1`: how many get each version, and text costs.
- Show both versions side by side with their counts. Launch follows the `/campaign` steps, only on their OK.
