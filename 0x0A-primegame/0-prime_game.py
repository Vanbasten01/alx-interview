#!/usr/bin/python3
""" Prime Game: Determine the winner based on prime number elimination """


def is_prime(n):
    """Check if n is prime"""
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def add_prime(n, primes):
    """Add primes up to n"""
    last_prime = primes[-1]
    if n > last_prime:
        for i in range(last_prime + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    """Determine winner based on prime elimination"""
    score = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]  # Pre-initialize list with first three primes
    add_prime(max(nums), primes)  # Add more primes if necessary

    for round in range(x):
        _sum = sum((i != 0 and i <= nums[round])
                   for i in primes[:nums[round] + 1])
        if (_sum % 2):
            winner = "Maria"
        else:
            winner = "Ben"
        if winner:
            score[winner] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"

    return None
