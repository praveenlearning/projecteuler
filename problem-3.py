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
    factor = 2
    if n % factor == 0:
        max_factor = factor
        while n % factor == 0:
            n = n // factor
    else:
        max_factor = 1
        factor += 1

    while n > 1 and factor <= sqrt(n):
        if n % factor == 0:
            max_factor = factor
            while n % factor == 0:
                n = n // factor
        factor += 2
    return max_factor if n == 1 else n


print(optimized(600851475143))
