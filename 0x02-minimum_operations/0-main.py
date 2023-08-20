#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 22
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 113
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 276
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 144
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
