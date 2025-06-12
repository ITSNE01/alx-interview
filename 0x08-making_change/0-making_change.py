#!/usr/bin/python3
""" Calculate the minimum number of coins needed to make a given total """


def makeChange(coins, total):
    """Return the fewest coins needed to reach total."""
    if total <= 0:
        return 0

    max_val = total + 1
    dp = [max_val] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                prev = dp[amount - coin]
                if prev + 1 < dp[amount]:
                    dp[amount] = prev + 1

    return dp[total] if dp[total] != max_val else -1
