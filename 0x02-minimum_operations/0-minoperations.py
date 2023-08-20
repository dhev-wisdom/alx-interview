#!/usr/bin/python3
"""
Minimum operations
"""


from typing import List, Union


def prime(num) -> bool:
    """
    Function check if number is prime or not
    """
    flag: bool = True
    if num == 1:
        flag = False
    elif num > 1:
        for i in range(2, int(num)):
            if (num % i) == 0:
                flag = False
                break
        else:
            flag = True
    else:
        flag = False
    return flag


def divisors(num: int) -> List[int]:
    """
    Function returns list of all numbers that can perfectly divide a number
    """
    divisors_list = []
    for i in range(2, num + 1):
        if num % i == 0:
            divisors_list.append(i)
    return divisors_list


def minOperations(n: int) -> int:
    """
    Minimum number of times to perform Copy All and Paste
    """
    if n <= 1:
        return 0
    elif n < 6 or prime(n):
        return n
    elif n >= 6 and not prime(n):
        divisors_ = divisors(n)
        first = divisors_[0]
        if first == 2 or n/first == 2:
            return minOperations(int(n/2)) + 2
        elif first != 2 and n/first != 2:
            return int(minOperations(first) + n/first)
