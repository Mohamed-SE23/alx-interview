#!/usr/bin/python3
"""
This Script determine the fewest number of
coins needed to meet a given amount
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed
    to meet a given total.

    :param coins: List of coin denominations.
    :param total: Target amount to make with the coins.
    :return: Fewest number of coins needed or -1 if the total cannot be met.
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
