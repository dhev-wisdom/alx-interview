#!/usr/bin/python3

"""
UTF-8 Validation
"""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Function determines if a given data set represents a valid UTF-8 encoding.
    """
    ans: bool = True
    for item in data:
        if item >= 256:
            ans = False
            break
    return ans
