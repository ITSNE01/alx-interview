#!/usr/bin/python3
"""
Determines if all locked boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of indexes representing a box,
        and each box contains a list of keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, or False.
    """
    if not isinstance(boxes, list):
        return False

    n = len(boxes)
    opened = set([0])
    keys = [0]

    while keys:
        current = keys.pop()
        for key in boxes[current]:
            if isinstance(key, int) and 0 <= key < n and key not in opened:
                opened.add(key)
                keys.append(key)

    return len(opened) == n
