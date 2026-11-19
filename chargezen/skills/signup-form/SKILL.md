---
name: signup-form
description: Build, publish, report on or turn off a SmartyTap sign-up form in Chargezen — a popup, flyout, embedded, full-page, banner or back-in-stock form that collects emails and phone numbers onto a list, with an optional offer or spin-to-win wheel — created as a draft, checked for anything that stops it going live, and published only on the merchant's OK. Use for "create a 10%-off email popup", "which popups are live", "how are my forms converting" or "turn off the winter popup".
argument-hint: "<what the form should do>"
---

# Sign-up form

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. See what's there

`chargezen.smartytap_forms.list.v1` (narrow with `query` or `status`): each form's type, whether it's live, scheduled, ended or a draft, its place in the order of forms that open on the store, and any A/B test. If a form already does what they want, offer to change it rather than add another: one popup, flyout, banner or full-page form shows per page view, so a second one competes with the first.

## 2. Results

`chargezen.smartytap_forms.report.v1` with the `form_ids`: viewers, sign-ups and sign-up rate, numbers that confirmed their texts, WhatsApp joins, shoppers per step, back-in-stock requests and alerts, credited orders and revenue, and a wheel's spins and prizes. **These figures are all time, since each form was made; there is no date range.** Say so, and don't present them as this month's.

## 3. Build it as a draft

1. **Pick a template** and create the draft with `chargezen.smartytap_forms.save.v1` (no `form_id`), the `template`, a name and a new `operation_id`. Shoppers see nothing yet.
2. `chargezen.smartytap_forms.get.v1` on the new form: its complete document, what stops it going live (`publish_errors`), and the real choices: the `lists` a step may join and the `discounts` an offer or wheel slice may give.
3. Change the document and send it back **whole** with `chargezen.smartytap_forms.save.v1` and the `form_id`; anything left out of a part you send is removed from it.
   - **The email step's list:** set it to a list from `get`'s `lists`, never a name you made up. Ask which list if it isn't clear.
   - **The offer:** a discount from `get`'s `discounts`, named exactly. If the code they want isn't there, it doesn't exist in their store yet: say so and don't invent one.
   - Headline and words in the store's voice; what they agree to (texts carry the terms the form shows); the success message saying what happens next.
4. Read `publish_errors` in the result. Fix each one, or tell the merchant what only they can provide.

Show the merchant, in plain words: the type and where it shows, the headline and offer, the list people join, and what they're sent after signing up (a text asking them to reply Y for numbers, a confirmation email for emails, as the workspace's consent settings send them).

## 4. Publish

Only when `publish_errors` is empty and the merchant says yes: `chargezen.smartytap_forms.publish.v1` with the `form_id`, now or with `live_from` and `live_until` for a schedule. If it's refused, nothing changed: fix what it names and ask again.

Then tell the merchant what the store needs, from the result:

- shoppers see forms only while the **Customer Events Pixel** app embed is on in the store's theme (`storefront_pixel`); if it isn't, they turn it on in Shopify's theme editor under App embeds;
- an **embedded** form also needs the "SmartyTap sign-up form" app block, with this form's id, added to a section of the theme;
- a **back-in-stock** form shows under the buy buttons of sold-out products, or in the "SmartyTap back in stock" app block.

## 5. Change, turn off, delete

- **Change a live form:** read it with `chargezen.smartytap_forms.get.v1` and save the whole document. A live form changes on the store at once, and a change that would stop it going live is refused; say so before saving. While an A/B test runs, the save changes version A.
- **Turn it off:** `chargezen.smartytap_forms.unpublish.v1`. It becomes a draft, shoppers stop seeing it at once, and its sign-ups and results stay. This is the right choice for "turn off the winter popup".
- **Delete** only when they want the form and its history gone: `chargezen.smartytap_forms.delete.v1` removes its results, wheel draws, credited orders and A/B tests for good, though the contacts it collected, their lists and consent stay. Recommend unpublishing instead, and confirm by the form's name before deleting.
