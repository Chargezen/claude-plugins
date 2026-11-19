---
name: failed-payments
description: Work the list of subscription renewals in Chargezen whose payment failed — who is still being retried, who ran out of retries, why each card failed, when it's tried next and roughly what's at risk — then send the customers you pick a secure link to update their card, on your OK. Use when they ask whose payment failed, about declined cards or dunning, or want to chase failed renewals now (for an automatic email-and-text flow, use /payment-recovery in the full Chargezen plugin).
argument-hint: "[retrying or ended, default both]"
---

# Failed payments

Which list: $ARGUMENTS (both if nothing was given).

Follow the `chargezen` skill for how to reach the tools. Covers renewals billed by Chargezen; Recharge and Stripe failures aren't on this list.

## 1. Read the lists

1. `chargezen.admin_subscriptions.failed_payments.v1` with `stage: "retrying"`, every page (`next_page` while `has_more`): charges still being retried or waiting on the store.
2. The same with `stage: "ended"`: charges that ran out of retries or that Chargezen couldn't complete.
3. For the lines worth the most attention (up to 20), `chargezen.admin_customer_subscriptions.get.v2` with the line's `customer_ref` and `subscription_ref`, for what they subscribe to and the price per order. The failed list itself carries no amount; say the total at risk is from the subscriptions you read.

## 2. Sort them

- **Waiting on the store** (`status: "blocked"`): read `block_reason`. These won't recover on their own; say what the store needs to fix.
- **Card problems** by reason (`reason`, as the payment provider recorded it): expired card, insufficient funds, declined, and so on. Expired and declined cards need a new card; insufficient funds often clear on the next retry.
- **Retrying:** when each is tried next (`next_retry_at`) and how many times it has failed.
- **Ended:** these renewals won't be charged again without the customer.

## 3. Report

Lead with one line: how many are retrying, how many ended, and the price per order at risk from what you read. Then a short table, ended first then by next retry: customer, what they subscribe to, reason, attempts, next retry. At most fifteen rows; say how many more.

## 4. Ask for new cards

Offer to send a card-update link to the customers who need one (ended, expired or declined). Show the list of names and say: **each customer gets an email from Shopify with a secure link to update the card for that subscription**. On a clear yes, `chargezen.admin_customer_subscriptions.request_payment_method_update.v1` for each, one at a time, passing the refs unchanged. If one returns an error (for example, the customer has several cards and must choose one in the subscription widget), note it and carry on. Report who was sent a link and who wasn't, and why. Never ask for or type card details.

Suggest `/payment-recovery` (full Chargezen plugin) if there's no automatic flow for failed payments yet.
