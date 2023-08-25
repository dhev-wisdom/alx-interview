#!/usr/bin/python3

"""
UTF-8 Validation
"""


from typing import List

def validUTF8(data):
    """
    UTF-8 Validation
    """
    num_bytes_to_follow = 0

    for byte in data:
        byte_value = byte & 0xFF

        if num_bytes_to_follow == 0:
            if (byte_value >> 7) == 0b0:
                continue
            elif (byte_value >> 5) == 0b110:
                num_bytes_to_follow = 1
            elif (byte_value >> 4) == 0b1110:
                num_bytes_to_follow = 2
            elif (byte_value >> 3) == 0b11110:
                num_bytes_to_follow = 3
            else:
                return False
        else:
            if (byte_value >> 6) != 0b10:
                return False
            num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0

