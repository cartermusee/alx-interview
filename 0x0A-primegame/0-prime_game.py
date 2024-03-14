#!/usr/bin/python3
"""module for Prime Game"""


def isWinner(x, nums):
    """determines the winner
    of a game played by Maria and Ben based on the given rules.
    """
    if x < 1 or not  nums:
        return None
    maria_wins = ben_wins = 0
    for num in nums:
        if num % 2 == 0:
            ben_wins += 1
            continue

        prime = next_prime(num)
        while prime <= num:
            if prime % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1
            num -= prime
            prime = next_prime(prime)
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None


def next_prime(num):
    """
    next prime number after the given number
    """
    while True:
        num += 1
        if is_prime(num):
            return num


def is_prime(num):
    """
    checks if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
