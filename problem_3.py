"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt

from util import benchmark


@benchmark
def optimized(n: int) -> int:
    """
    :param n: number
    :return: the largest prime factor

    divide number by each prime number to get the largest prime factor
    """
    n_ = n
    factor = 2
    if n_ % factor == 0:
        max_factor = factor
        while n_ % factor == 0:
            n_ = n_ // factor
    else:
        max_factor = 1
    factor += 1

    while n_ > 1 and factor <= sqrt(n):
        if n_ % factor == 0:
            max_factor = factor
            while n_ % factor == 0:
                n_ = n_ // factor
        factor += 2
    return max_factor if n_ == 1 else n_


print(optimized(600851475143))
