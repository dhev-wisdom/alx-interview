#!/usr/bin/python3
"""
determine the fewest number of coins needed to meet a given amount
"""

from typing import List
import math


def makeChange(coins: List[int], total: int) -> int:
    """
    Return the fewest number of `coins` needed to meet `total`
    """
    if total <= 0:
        return 0
    coins.sort()
    if len(coins) == 0 or coins[len(coins) - 1] == 0:
        return 0
    times = 0
    for i in range(len(coins) - 1, 0, -1):
        if i == 0 and total != 0:
            return -1
        ans = total / coins[i]
        ans = math.floor(ans)
        if ans < 1:
            continue
        times += ans
        total = total - (coins[i] * ans)
        continue
    if total == 0:
        return times
    else:
        return -1