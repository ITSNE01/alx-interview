#!/usr/bin/python3
"""
    Provides minOperations function to calculate the fewest
    Copy All and Paste operations needed to reach n 'H' characters.
"""


def minOperations(n):
    """
        Calculates the minimum number of operations (Copy All and Paste)
        needed to reach n 'H' characters starting from a single 'H'.

    Parameters:
        n (int): target number of 'H' characters.

    Returns:
        int: minimum number of operations, or 0 if n < 2.
    """
    if n < 2:
        return 0

    ops = 0
    divisor = 2
    # Factorize n and sum its prime factors
    while divisor * divisor <= n:
        while n % divisor == 0:
            ops += divisor
            n //= divisor
        divisor += 1

    # If remaining n is prime, add it
    if n > 1:
        ops += n

    return ops
