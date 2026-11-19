---
name: points
description: Look up and change one customer's loyalty points in Chargezen — balance, tier, points about to expire and rewards issued; add points as a thank-you or goodwill gesture, take points off, redeem points for a reward on their behalf, or undo a mistake. Use when someone asks about a customer's points or wants them changed.
argument-hint: "<customer> [what to do]"
---

# Points

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

1. **Find the customer:** `chargezen.customers.search.v1`; confirm the right person.
2. **Show their account:** `chargezen.admin_rewards.get_customer.v1`: balance, tier and what the next tier needs, points expiring in the next 30 days, and rewards issued with whether they've been used. For "where did these points come from", `chargezen.admin_rewards.customer_history.v1`.
3. **Change it**, on the merchant's OK, with a new `operation_id` and a reason the customer can read:

| They want | Tool | Watch for |
|---|---|---|
| Add points (thank-you, goodwill, a missed purchase) | `chargezen.admin_rewards.adjust_points.v1` with a positive number | The customer may get the store's points-earned email |
| Take points off | `chargezen.admin_rewards.adjust_points.v1` with a negative number | The balance can go below zero |
| Redeem for a reward for them | `chargezen.admin_rewards.get_program.v1` for the rewards, then `chargezen.admin_rewards.redeem.v1` | Show the cost in points and what they get |
| Undo a manual deduction | `chargezen.admin_rewards.reverse_adjustment.v1` | |
| Undo points that shouldn't have been given | `chargezen.admin_rewards.void_points.v1` | |
| Bring back voided points | `chargezen.admin_rewards.restore_points.v1` | |
| Cancel a reward coupon | `chargezen.admin_rewards.void_reward.v1`; to return its points, `chargezen.admin_rewards.refund_reward.v1` | |

A balance change can move the customer to another tier and update their tier tag in Shopify; say so when it will.

4. Read `chargezen.admin_rewards.get_customer.v1` again and report the new balance and tier.
