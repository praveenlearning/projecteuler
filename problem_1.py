"""
Multiples of 3 or 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import functools
import itertools

from util import benchmark


@benchmark
def normal(n: int) -> int:
    sum_n = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum_n += i
    return sum_n


@benchmark
def approach_2(n: int) -> int:
    filtered = filter(lambda x: x % 3 == 0 or x % 5 == 0, range(n + 1))
    return sum(filtered)


@benchmark
def optimized(n: int) -> int:
    """
    :param n: number
    :return: sum of all numbers within the provided number divisible by divisors

    uses arithmatic progression formula to calculate the sum
    """
    divisors = [3, 5]
    sum_n = 0

    for i in range(len(divisors)):
        comb = itertools.combinations(divisors, i + 1)
        for each in comb:
            value = functools.reduce(lambda x, y: x * y, each)
            count = n // value
            sum_n += (1 if len(each) % 2 != 0 else -1) * (value * (count * count + count) // 2)
    return sum_n


number = 999

print(normal(number))
print(approach_2(number))
print(optimized(number))
