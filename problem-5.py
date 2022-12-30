"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math
from functools import reduce
from math import sqrt

from util import benchmark


def prime_factors(n: int):
    factors = {}
    factor = 2
    if n % factor == 0:
        count = 0
        while n % factor == 0:
            count += 1
            n = n // factor
        factors[factor] = count
    factor += 1

    while n > 1 and factor <= sqrt(n):
        if n % factor == 0:
            count = 0
            while n % factor == 0:
                count += 1
                n = n // factor
            factors[factor] = count
        factor += 2
    if n != 1:
        factors[n] = 1
    return factors


def is_prime(n: int) -> bool:
    if n == 1:
        return False
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True


@benchmark
def approach_1() -> int:
    all_factors = {}
    for i in range(2, 21):
        i_factors = prime_factors(i)
        for i_factor, i_count in i_factors.items():
            all_factors[i_factor] = max(i_count, all_factors.get(i_factor, 0))

    return reduce(lambda x, y: x * y[0] ** y[1], all_factors.items(), 1)


@benchmark
def approach_2() -> int:
    k = 20
    primes = filter(is_prime, range(2, k + 1))
    n = 1
    limit = sqrt(k)
    check = True
    for prime in primes:
        a = 1
        if check:
            if prime <= limit:
                a = math.floor(math.log(k, prime))
            else:
                check = False
        n = n * (prime ** a)
    return n


print(approach_1())
print(approach_2())
