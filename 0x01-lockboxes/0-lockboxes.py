#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """
    Function tests if all boxes can be opened
    """
    opened_boxes = {0}
    keys_to_check = [0]

    while keys_to_check:
        current_box = keys_to_check.pop()
        for key in boxes[current_box]:
            if key not in opened_boxes:
                opened_boxes.add(key)
                keys_to_check.append(key)

    return len(opened_boxes) == len(boxes)
