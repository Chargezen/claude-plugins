---
name: survey
description: Build a SmartyTap survey in Chargezen — "how did you hear about us", a 0-10 "would you recommend us" score, a product feedback or birthday question, with an optional free gift — saved as a draft, put live on the merchant's OK, sent by email, text or an Ask-by-text flow step, and read back as results. Answers can save to the contact's profile for segments and flows. Use for attribution surveys, NPS, customer feedback, zero-party data or survey results.
argument-hint: "<what to ask> [who, free gift]"
---

# Survey

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Check what's there

`smartytap_surveys.list`: each survey's status and how many answered. If one already asks this, offer to reuse or edit it (`smartytap_surveys.get`, then `update`), or just read its results (step 5).

## 2. Write it

Keep it short: one to three questions finish far more often than ten.

- **Question types:** `single_choice` and `multiple_choice` (with answers, and an Other answer people write in), `rating` (1–5), `nps` (0–10), `short_text`, `long_text`, `email`, `number`, `date`.
- **Save answers to the profile** with a `property` (such as `heard_about_us`, `skin_type`, `birthday`), so segments (`/segment`) and flows can use them. A `date` question saved as `birthday` feeds `/birthday-flow`.
- **Common ones:**
  - *How did you hear about us?* single choice: Instagram, TikTok, a friend, Google, a podcast, Other.
  - *How likely are you to recommend us?* NPS 0–10, then an optional "What's the main reason?" long text.
- **Who answers:** ask for an email unless the link already knows who they are (a survey with a free gift always asks). Optional response limit or closing date.
- **Free gift** (optional): real products from `products.search`, given when claimed, which become real orders. Say that cost plainly.
- **Thank-you** heading and text.

Show the person the whole survey as respondents will see it.

## 3. Save and put live

1. `smartytap_surveys.create` with the definition and a new `operation_id`. It's a draft and takes no answers. The result lists what still stops it going live; fix those with `smartytap_surveys.update` (from the revision you read).
2. On their OK: `smartytap_surveys.publish`. It now takes answers on its own page (`page_url`, which its link and QR code open). Where it shows on the store is set in SmartyTap's survey editor.

## 4. Get it to people

- **A campaign** linking the page (`/campaign`), or a link in an existing flow email.
- **A flow:** an **Ask by text** step (`ask_text`) texts one question of the live survey and follows each answer down its own path, with paths for any other reply and no reply. Good after an order ships (`/order-follow-up`). Texts are marketing, so only people who agreed to texts get them.
- **A thank-you flow** on **Answered a survey** (`smartytap.survey.answered`), filtered on `answers`, for example a review request to people who scored 9 or 10 and an internal alert to the team for low scores.

## 5. Read the results

`smartytap_surveys.results` for a range of days (30 by default, at most 366): how many saw it and answered, the response rate, free gifts claimed and turned into orders, and each question's answers (counts per answer, the rating spread and average, the NPS score). Written answers aren't included in results; say so. Lead with the headline ("Most new customers heard about you on …", "NPS is …") and one thing to do about it.
