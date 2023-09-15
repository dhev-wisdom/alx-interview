#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """rotate a 2D matrix 90 degrees clockwise"""
    a = 0
    for list_ in matrix:
        if a == 0:
            for idx in range(len(list_)):
                matrix[idx].append(list_[0])
                list_.pop(0)
        elif a == 1:
            for idx in range(len(list_)):
                if idx == 0:
                    matrix[idx].insert(idx, list_[idx])
                    list_.pop(idx)
                if idx == 2:
                    matrix[idx].insert(1, list_[1])
                    list_.pop(1)
        elif a == 2:
            for idx in range(len(list_)):
                if idx == 0:
                    matrix[idx].insert(0, list_[idx])
                    list_.pop(idx)
                elif idx == 1:
                    matrix[idx].insert(0, list_[idx])
                    list_.pop(idx)
                elif idx == 2:
                    matrix[idx].insert(0, list_[1])
                    list_.pop(idx)
        a += 1
