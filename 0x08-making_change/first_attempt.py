#!/usr/bin/python3
"""
determine the fewest number of coins needed to meet a given amount
"""

from typing import List
import math
import time


def makeChange(coins: List[int], total: int) -> int:
    """
    Return the fewest number of `coins` needed to meet `total`
    """
    print("Mine")
    start_time = time.time()
    if total <= 0:
        print("Took total of {} seconds".format(time.time() - start_time))
        return 0
    coins.sort()
    if len(coins) == 0 or coins[len(coins) - 1] == 0:
        print("Took total of {} seconds".format(time.time() - start_time))
        return 0
    times, iterations = 0, 0
    for i in range(len(coins) - 1, 0, -1):
        iterations += 1
        print("Nummber of iterations: ", iterations)
        if i == 0 and total != 0:
            print("Took total of {} seconds".format(time.time() - start_time))
            return -1
        ans = total / coins[i]
        ans = math.floor(ans)
        if ans < 1:
            continue
        times += ans
        total = total - (coins[i] * ans)
        print("Iteration got down")
        continue
    if total == 0:
        print("Took total of {} seconds".format(time.time() - start_time))
        return times
    else:
        print("Took total of {} seconds".format(time.time() - start_time))
        return -1
    