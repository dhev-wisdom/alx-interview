#!/usr/bin/python3


def validUTF8(data):
    try:
        bytes(data).decode()
        return True
    except BaseException:
        return False
