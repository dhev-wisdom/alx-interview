#!/usr/bin/python3
"""
determine the fewest number of coins needed to meet a given amount
"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Return the fewest number of `coins` needed to arive at `total`
    """
    if not coins:
        return -1
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    if len(coins) == 0 or coins[0] == 0:
        return 0
    num_coins, remaining_total = 0, total
    for coin in coins:
        if coin == 0:
            continue
        if remaining_total == 0:
            break
        number_of_coins = remaining_total // coin
        num_coins += number_of_coins
        remaining_total -= number_of_coins * coin
    if remaining_total == 0:
        return num_coins
    else:
        return -1
