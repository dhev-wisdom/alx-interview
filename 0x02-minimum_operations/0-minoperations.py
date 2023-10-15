#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n: int) -> int:
    """
    Minimum operations
    """
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            n //= divisor
            operations += divisor

        divisor += 1

    return operations
