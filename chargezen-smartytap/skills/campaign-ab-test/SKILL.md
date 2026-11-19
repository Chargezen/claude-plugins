---
name: campaign-ab-test
description: Set up an A/B test on a SmartyTap campaign email or text in Chargezen — two or more subject lines, versions of the content or versions of a text, or a test of send times — choosing the test size, how long it runs and how the winner is picked, then read how each version is doing and end the test early by picking the winner on the merchant's OK. Use for subject-line tests, content tests, testing two texts, best-time-to-send tests, or "which version is winning?".
argument-hint: "<campaign> [what to test]"
---

# Campaign A/B test

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Pick what to test

Test one thing at a time, so the result means something:

- **Subject line** (most common): same email, different subject or preview text. Winner by `open_rate`.
- **Content:** a different headline, offer or button. Winner by `click_rate` (needs click tracking on) or `placed_order_rate`.
- **A text:** two or more wordings of the same text. Winner by `click_rate` (needs click tracking on) or `placed_order_rate` (the share of test sends that ordered after receiving it).
- **Send time:** everyone gets the same email on the scheduled day, split across two to six local times, and the report compares them; no winner is picked. It needs a scheduled-once send and can't be combined with an A/B test on the same message.

Small audiences don't give a clear answer. Check `chargezen.smartytap_campaigns.preview_audience.v1` first; with only a few hundred recipients, suggest a send-time test or no test.

## 2. Set it up on a draft

1. `chargezen.smartytap_campaigns.get.v1` (it must be a draft; versions can't be added once it's scheduled).
2. Make the versions:
   - **An email:** `chargezen.smartytap_campaigns.add_versions.v1` with the email's message id and the total number of versions (2 for A and B). Each starts as a copy of the email. Change each version at its own document address with `chargezen.email_documents.apply_ops.v1` (`set_subject`, `set_preheader` or the blocks being tested).
   - **A text:** write them inline in the text's `versions` with `chargezen.smartytap_campaigns.create.v2` or `chargezen.smartytap_campaigns.update.v2`. Version A is the text's `body`; `versions` holds B, C and so on, each its own text written the same way. An empty `versions` removes them; leaving it out keeps the saved ones. `chargezen.smartytap_campaigns.add_versions.v1` is for emails only.
3. **Texts cost more with versions.** Each version is a paid text priced by its own length, and the test group is charged like any send; `chargezen.smartytap_campaigns.preview_audience.v1` prices the not-yet-known winner at the longest version. Show the merchant the higher cost and get their OK on it before launch.
4. Set the test in the message's `ab_test` with `chargezen.smartytap_campaigns.update.v2` (read the revision first): `test_size_percent` (10–100; at 100 everyone gets one of the versions and no winner is picked; 20–30 is common), `duration_hours` (1–72; 4 or more for opens, longer for orders), and `metric`. For a send-time test, set `send_time_test` with the times instead.
5. `chargezen.smartytap_campaigns.review.v1` and `chargezen.smartytap_campaigns.preview.v2`; show the person each version, the test settings and in one sentence what happens ("30% get A or B; after 6 hours the one with more opens goes to the other 70%"). A version they don't want: for an email, `chargezen.smartytap_campaigns.remove_version.v1`; for a text, save its `versions` without it.

Launch follows the `/campaign` steps, only on their OK.

## 3. While it runs

`chargezen.smartytap_campaigns.report.v1`: each version's sends, opens, clicks, orders and revenue, its test figures by the winner's `metric` (`test`: sends, how many reached the metric, and the rate), and the test's state (`testing`, `decided`, `split`). Where the assistant shows interactive views it opens as one; it presents the same figures, so still give them in words and never send the merchant to the admin to see them. Give the numbers and the rates you work out from them, and say if the gap is too small to trust yet.

To end it early, only on their OK: `chargezen.smartytap_campaigns.choose_winner.v1` with the email's or text's message id and the winning version's `variant_id` from the report. Everyone still waiting gets that version now (within the campaign's timing and quiet hours; each text is paid from the SMS credit). Otherwise do nothing: the test picks the winner by its own rule.

## 4. Keep what worked

For an email, offer to save the winner as a template (`chargezen.smartytap_email_templates.create_from_email.v2` with the winning version's address) and to note the lesson for the next campaign.
