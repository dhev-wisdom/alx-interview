#!/usr/bin/python3

import sys

def prime(num):
    """
    Prime number
    """
    flag = True
    if num == 1:
        flag = False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break
        else:
            flag = True
    else:
        flag = False

    return flag


if __name__ == '__main__':
    print(prime(int(sys.argv[1])))
