#!/usr/bin/python3
"""module for min operations"""


def minOperations(n):
    """takes a number n

    Keyword arguments:
    n: the number
    Return: operations
    """
    if n == 1:
        return 0

    def smallest_prime_factor(num):
        """small prime num
        Keyword arguments:
        num: the number
        Return: num
        """
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return i
        return num

    operations = 0
    divisor = smallest_prime_factor(n)

    while n > 1:
        if divisor == n:
            operations += n
            break

        while n % divisor == 0:
            n //= divisor
            operations += divisor

        divisor = smallest_prime_factor(n)

    return operations
