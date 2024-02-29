#!/usr/bin/python3
"""module for make change"""


def makeChange(coins, total):
    """function for make change"""
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]