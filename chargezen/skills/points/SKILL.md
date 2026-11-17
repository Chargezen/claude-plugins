---
name: points
description: Look up and change one customer's loyalty points in Chargezen — balance, tier, points about to expire and rewards issued; add points as a thank-you or goodwill gesture, take points off, redeem points for a reward on their behalf, or undo a mistake. Use when someone asks about a customer's points or wants them changed.
argument-hint: "<customer> [what to do]"
---

# Points

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

1. **Find the customer:** `customers.search`; confirm the right person.
2. **Show their account:** `admin_rewards.get_customer`: balance, tier and what the next tier needs, points expiring in the next 30 days, and rewards issued with whether they've been used. For "where did these points come from", `admin_rewards.customer_history`.
3. **Change it**, on the merchant's OK, with a new `operation_id` and a reason the customer can read:

| They want | Tool | Watch for |
|---|---|---|
| Add points (thank-you, goodwill, a missed purchase) | `adjust_points` with a positive number | The customer may get the store's points-earned email |
| Take points off | `adjust_points` with a negative number | The balance can go below zero |
| Redeem for a reward for them | `admin_rewards.get_program` for the rewards, then `redeem` | Show the cost in points and what they get |
| Undo a manual deduction | `reverse_adjustment` | |
| Undo points that shouldn't have been given | `void_points` | |
| Bring back voided points | `restore_points` | |
| Cancel a reward coupon | `void_reward`; to return its points, `refund_reward` | |

A balance change can move the customer to another tier and update their tier tag in Shopify; say so when it will.

4. Read `get_customer` again and report the new balance and tier.
