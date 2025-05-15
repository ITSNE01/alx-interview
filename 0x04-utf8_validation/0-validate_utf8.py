#!/usr/bin/python3
"""
UTF-8 Validation

This module provides a function validUTF8 that determines
if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determine if a list of integers is valid UTF-8.

    Args:
        data (list of int): Each int represents one byte.

    Returns:
        bool: True if valid UTF-8 encoding, otherwise False.
    """
    n = len(data)
    i = 0

    while i < n:
        """Only lowest 8 bits of each integer"""
        byte = data[i] & 0xFF

        """Count leading 1 bits in byte"""
        mask = 0b10000000
        count = 0
        while mask & byte:
            count += 1
            mask >>= 1

        """1-byte character (ASCII)"""
        if count == 0:
            i += 1
            continue

        """Leading byte must have 2-4 leading 1s"""
        if count == 1 or count > 4:
            return False

        """Not enough bytes left"""
        if i + count > n:
            return False

        """Check continuation bytes"""
        for j in range(i + 1, i + count):
            cont = data[j] & 0xFF
            """Continuation bytes must start with '10'"""
            if cont >> 6 != 0b10:
                return False

        i += count

    return True
