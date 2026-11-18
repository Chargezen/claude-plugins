---
name: upsell-results
description: Read how the merchant's checkout and post-purchase upsells performed in Chargezen CheckoutOS over a period — views, take rate, revenue and revenue per view for every offer, each post-purchase funnel step, and every A/B test's control against challenger — then pick the winners and end finished tests on their OK. Use when they ask how their upsells are doing, which offer underperforms, whether a test has a winner, or to end an upsell experiment.
argument-hint: "[days, default 30]"
---

# Upsell results

Window: the last $ARGUMENTS days (30 if no number was given), with the store's UTC offset on both ends.

Follow the `chargezen` and `checkoutos` skills for how to reach the tools. **Read only** until the person picks a winner.

## 1. Read

1. `upsell_analytics.get` with `from` and `to`: each offer with shopper events in the window (impressions, accepted, declined, purchased, revenue, conversion rate, revenue per impression), and every experiment with its control and challenger arms.
2. `post_purchase_upsells.funnels` for the same dates: each post-purchase offer's visits, acceptances, declines, revenue and conversion, its accepted and declined next steps, and whole-funnel totals.
3. `upsell_experiments.list` with `status: "running"` for the tests still splitting shoppers.
4. `checkout_upsells.list` and `post_purchase_upsells.list` for active offers with no events in the window. Then `checkout_extensions.discover`: an active offer with no views often means its block isn't on the checkout.

Checkout revenue counts purchased upsells; post-purchase revenue counts accepted ones. Offers with only a handful of views can't be judged yet; say so instead of ranking them.

## 2. Report

- **Headline:** total upsell revenue in the window, the best offer by revenue per view, and the weakest offer with real traffic.
- **Offers:** a short table (offer, where it shows, views, take rate, revenue, revenue per view), best first, at most ten rows.
- **Funnels:** for each funnel, where shoppers drop off.
- **Tests:** for each running test, both arms side by side (buyers, converted, revenue per buyer) and whether one is clearly ahead or it needs more time. Don't call a winner on small numbers.
- **Not showing:** active offers with no views, and why if discover says.

## 3. End a test

For a test with a clear result, say what ending it does before asking:
- **challenger wins:** the challenger goes live with the original's priority and targeting, and the original goes back to draft;
- **control wins or no winner:** nothing changes; the original keeps showing to everyone.

On a clear yes, `upsell_experiments.end` with the experiment and the winner. For a checkout test, `checkout_upsells.get` afterwards to confirm the discount republished, and report any error plainly.

Offer the next step: test the weakest offer (`/upsell-experiment`), or a full checkout review (`/checkout-audit`).
