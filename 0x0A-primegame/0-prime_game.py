#!/usr/bin/python3
"""
Determine the winner of the Prime Game across multiple rounds.
"""


def isWinner(x, nums):
    """
    Determine who wins the most rounds of the prime game.

    Args:
        x (int): number of rounds to play.
        nums (list of int): list of n values for each round.

    Returns:
        str: "Maria" or "Ben" if there is a clear winner, else None.
    """
    if x <= 0 or not nums:
        return None

    rounds = nums[:x]
    max_n = max(rounds)

    sieve = [True] * (max_n + 1)
    sieve[0:2] = [False, False]

    p = 2
    while p * p <= max_n:
        if sieve[p]:
            for multiple in range(p * p, max_n + 1, p):
                sieve[multiple] = False
        p += 1

    prime_counts = [0] * (max_n + 1)
    total = 0
    for i in range(max_n + 1):
        if sieve[i]:
            total += 1
        prime_counts[i] = total

    maria = 0
    ben = 0
    for n in rounds:
        if prime_counts[n] % 2:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
