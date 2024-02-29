#!/usr/bin/python3
"""This module provides a function to determine the fewest
     number of coins needed to meet a given total amount."""


def makeChange(coins, total):
    """Determine the fewest number of coins needed
         to meet a given total amount."""
    if total <= 0:
        return 0
    count = 0
    for coin in coins[::-1]:
        while total / coin >= 1:
            count += 1
            total -= coin
    if total == 0:
        return count
    return -1
