#!/usr/bin/python3
"""module for make change"""


def makeChange(coins, total):
    """function for make change"""
    if total <= 0:
        return 0

    least_Coin = [float('inf')] * (total + 1)
    least_Coin[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            if least_Coin[amount - coin] + 1 < least_Coin[amount]:
                least_Coin[amount] = least_Coin[amount - coin] + 1

    if least_Coin[total] == float('inf'):
        return -1
    else:
        return least_Coin[total]
