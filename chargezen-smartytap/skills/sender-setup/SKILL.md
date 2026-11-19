---
name: sender-setup
description: Get a Chargezen workspace ready to send SmartyTap texts and emails — set texting up from nothing (business details, verification contact, a first toll-free number and its carrier verification, local-texting registration), add, rename, pause or release numbers, choose the countries it texts, and set up the store's own email domain, footer, team mailbox and default sender. Nothing is bought, submitted to carriers or released without an explicit OK on the exact item. Use when texts or emails can't send yet, a carrier turned texting down, they want another number or country, or campaigns should come from the store's own address.
argument-hint: "[texting | number | countries | email]"
---

# Sender setup

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Where things stand

1. `chargezen.smartytap_sms.get_setup.v1`: whether the workspace can text now and, if not, its `blockers`; the business details and verification contact carriers check; the countries it texts; every texting number with its carrier review, the carriers' reason when they turned it down, and whether it can text; and the local-texting registration with its status, starting values and fees.
2. `chargezen.smartytap_campaigns.authoring_options.v1`: the `sms` answer (whether campaign texts can go out now) and the email senders campaigns can use.
3. For email: `chargezen.email_channel.list_domains.v1` (the store's own sending domains, the DNS records each needs and whether they pass) and `chargezen.email_channel.list_mailboxes.v1` (each mailbox, whether it can send and which is the default sender).

Tell the person in two lines what's ready and what isn't, then work on what they asked for.

## 2. Texting from nothing

A workspace's first number is a toll-free number, and carriers must verify it before it texts. Work through the `blockers` in order:

1. **Business details:** show the privacy policy address and the automatic replies for HELP, STOP and START from `business_details` (suggested text where nothing is saved). Say that the replies apply at once to everyone who texts those words. On their OK, `chargezen.smartytap_sms.save_business_details.v1`.
2. **Verification contact:** ask for the person carriers can reach and the business's US street address. `chargezen.smartytap_sms.save_verification_contact.v1`; if it lists missing fields, ask for just those.
3. **The number:** ask the country (or countries) it will text. `chargezen.smartytap_sms.search_numbers.v1` with `number_type: "toll_free"`; show every result and let the merchant choose. Never pick for them.
4. **The verification:** `chargezen.smartytap_sms.draft_toll_free_verification.v1` writes it from the workspace's own records. Show it in plain words: what the store texts about, the example texts, how people sign up and what they agree to, and the monthly volume. Ask for a link to a screenshot of the sign-up form that collects phone numbers (the draft has none), and take their corrections. Pick `use_case` and `message_volume` only from the choices it returns.
5. **Confirm both:** the number carries a **monthly cost** (these tools give no price, so don't quote one), and the verification goes to the carriers exactly as written. Only after an explicit OK on that number and that text: `chargezen.smartytap_sms.register_toll_free_number.v1` with the number, the countries and the verification.
6. Tell them what happens next: carriers usually answer in the time the draft's `typical_wait` gives (often 3 to 5 business days), the workspace is emailed when they do, and the number texts only once approved.

**Turned down:** `chargezen.smartytap_sms.get_setup.v1` shows the carriers' `reason` and `fix`. Correct the verification with the merchant and call `chargezen.smartytap_sms.register_toll_free_number.v1` again with the same number; a number the workspace already has isn't bought again.

## 3. Local (area-code) numbers

Local numbers text only after the business is registered for local texting with US carriers, and need a first number already in place (section 2).

1. Start from `local_texting.defaults` in `chargezen.smartytap_sms.get_setup.v1`; ask only for what's missing, such as the EIN.
2. Show the form and the fees from `local_texting.fees`: what's due today and the monthly fee that follows until the registration ends.
3. On their OK, `chargezen.smartytap_sms.register_local_texting.v1`. It submits nothing yet: it returns a payment link for a teammate who may pay workspace bills to open in their own browser (if `can_pay` is false, the workspace owner at `owner_email` pays). Never pay for them. Once paid, the form goes to carriers; approval usually takes one to two weeks and the workspace is emailed.

Refused while a registration is in review or already approved: say so and show where it stands.

## 4. Another number

1. Ask: which country, local or toll-free, and for local an area code if they care.
2. `chargezen.smartytap_sms.search_numbers.v1`: up to ten numbers. Show them all; let the merchant choose.
3. Say plainly before buying: every number carries a **monthly cost**, so add only the numbers they need, and a new local number texts only once the local-texting registration covers it (a toll-free one, once carriers verify it).
4. Only after they confirm the exact number: `chargezen.smartytap_sms.buy_number.v1` with that number and an optional label (such as "Chicago store"). If it's gone, search again and let them choose again.

## 5. Change or give up a number

- **Rename, make primary or pause:** `chargezen.smartytap_sms.update_number.v1`. Pausing (`active: false`) stops texts in and out at once, but the number stays and keeps its monthly cost.
- **Give it up for good:** `chargezen.smartytap_sms.release_number.v1` ends texts and calls on it at once, ends its cost, and the number may never come back. Only after an explicit OK on that exact number.

## 6. Countries

`chargezen.smartytap_sms.set_countries.v1` replaces the whole list, shared by every number. Show the list now and the list after; texts to a country left out are refused by carriers, and it can't leave out a country one of its own numbers texts from. Only on their OK.

## 7. Email from the store's own address

1. **Domain:** if `chargezen.email_channel.list_domains.v1` has no domain sending campaigns, ask which domain (such as `brand.com` or `mail.brand.com`) and on their OK `chargezen.email_channel.add_domain.v1` with `sends: "marketing"`. It returns the DNS records to add.
2. **DNS records are the merchant's step:** list each record (type, name, value) and ask them to add it at their domain provider. Once they say it's done, `chargezen.email_channel.check_domain.v1`; new records can take up to an hour to show, so if some still fail, say which and check again later.
3. **Footer:** campaign emails show a postal address in their footer, the store address unless the domain has its own. To set one, `chargezen.email_channel.update_footer.v1` on their OK.
4. **Team sender:** `chargezen.smartytap_senders.add_team_sender.v1` with an address on a verified sending domain (such as `news@brand.com`) and a From name. Replies arrive in the inbox.
5. **Default sender:** `chargezen.email_channel.set_default_sender.v1` makes a team mailbox the one new campaigns send from when nobody picks one. Say before saving that customer order and subscription emails also switch to it once it can send.

End with what's ready now and the next step, such as a first `/campaign` or `/welcome-series`.
