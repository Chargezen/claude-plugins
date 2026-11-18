---
name: sender-setup
description: Get a Chargezen workspace ready to send SmartyTap texts and emails — check what texting setup still needs, choose the countries it texts, search for a local or toll-free number and add the exact one the merchant picks, and add a team mailbox such as news@brand.com for campaign emails. Nothing is bought without an explicit OK on the exact number. Use when texts can't send yet, they want another number or country, or they want campaigns to come from a team address.
argument-hint: "[texting | number | countries | email sender]"
---

# Sender setup

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Where things stand

1. `smartytap_campaigns.authoring_options`: the `sms` answer says whether campaign texts can go out now, and if not, why, the step to take (`fix`) and the SmartyTap page for it (`url`), plus the countries the numbers text and the email senders.
2. `inbox.senders`: the texting numbers, whether each is ready to text and which is primary.

Tell the person in two lines what's ready and what isn't.

## 2. The first number and registration

The workspace's **first** texting number, and carrier registration (local-texting registration for local numbers, carrier review for toll-free), are done in SmartyTap's SMS setup, not here: give them the `fix` and the `url` from the options. Adding a number is refused until that first number is set up.

## 3. Another number

1. Ask: which country, local or toll-free, and for local an area code if they care.
2. `smartytap_sms.search_numbers`: up to ten numbers. Show them all; let the merchant choose. Never pick for them.
3. Say plainly before buying: every number added carries a **monthly cost**, so add only the numbers they need, and a new local number still needs local-texting registration (toll-free, carrier review) before it texts. These tools give no price, so don't quote one.
4. Only after they confirm the exact number: `smartytap_sms.buy_number` with that number and an optional label (such as "Chicago store"). If it's gone, search again and let them choose again. Asking again for a number the workspace already has buys nothing.

## 4. Countries

`smartytap_sms.set_countries` replaces the whole list, shared by every number. Show the list now and the list after; texts to a country left out are refused by carriers, and it can't leave out a country one of its own numbers texts from. Only on their OK.

## 5. A team email sender

`smartytap_senders.add_team_sender` with an address on one of the workspace's own sending domains (such as `news@brand.com`) and a From name. Replies arrive in the inbox. It's refused when the domain isn't added and verified in **Settings → Email**; send them there first. Afterwards it shows among the senders campaigns and flows can use.

End with what's ready now and the next step, such as a first `/campaign` or `/welcome-series`.
