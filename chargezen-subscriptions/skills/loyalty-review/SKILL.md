---
name: loyalty-review
description: Review the merchant's Chargezen loyalty program — how customers earn points, what they can redeem, VIP tiers, referrals and the rewards emails — against how customers actually use it, then recommend the few changes worth making and save them as drafts, publishing only on their OK. Use when they ask whether their rewards program is working, how to improve it, or want to add a tier, reward or way to earn.
argument-hint: "[what to focus on]"
---

# Loyalty review

Focus, if given: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Read the program

- `chargezen.admin_rewards.get_program.v1`: every way to earn, every reward, referrals and tiers, active or not. If there's no program, or `active` is false, say so first: customers aren't earning anything yet. Offer to set it up, then turn it on with `chargezen.admin_rewards.save_program.v1` only on their OK.
- `chargezen.admin_rewards.history.v1` with `source: "redemptions"` (a few pages): which rewards people actually take, and how many issues failed or were voided.
- `chargezen.admin_rewards.history.v1` with `source: "points"` (a few pages): where points come from.
- `chargezen.admin_rewards.history.v1` with `source: "tiers"`: how many customers reach each tier.
- `chargezen.notification_emails.list.v1`: which rewards emails exist and are on.
- `chargezen.rewards_surfaces.get.v1`: what the rewards page and launcher show.

History is recorded activity in Chargezen, newest first; say how far back the pages you read go.

## 2. Find what to change

Look for, and back each with a number from what you read:

- rewards nobody redeems (too expensive, or not wanted)
- one reward taking almost all redemptions (offer a step up)
- ways to earn that never fire, or that are switched off
- a tier almost nobody reaches, or one everybody reaches
- referrals off, or a referral reward below the cheapest redemption
- rewards emails that are off, or missing for points earned or rewards ready

Recommend **three changes at most**, ranked by how many customers they reach. For each: what to change, why (the number), and what customers will notice.

## 3. Make the changes

Only the ones they approve, one at a time, reading the definition before you replace it:

- earning: `chargezen.admin_rewards.save_earn_definition.v1`
- rewards: `chargezen.admin_rewards.save_redemption_definition.v1`
- tiers: `chargezen.admin_rewards.save_tier.v1`
- referrals: `chargezen.admin_rewards.save_referral_definition.v1`
- emails: `chargezen.notification_emails.save.v1`, then `chargezen.notification_emails.preview.v1`, and `chargezen.notification_emails.send_test.v1` to them before turning one on

If the rewards page needs to show the change, `chargezen.rewards_surfaces.save.v1` the draft, show what changes, and `chargezen.rewards_surfaces.publish.v1` only when they say so. Deleting a definition or tier can't be undone: ask first, every time.
