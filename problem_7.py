"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
import itertools

from util import benchmark, is_prime


@benchmark
def normal(nth: int) -> int:
    nth_prime = 0
    if nth == 1:
        nth_prime = 2

    """2 is counted so subtract 1"""
    nth -= 1

    number_ = 3
    while nth > 0:
        if is_prime(number_):
            nth_prime = number_
            nth -= 1
        number_ += 2

    return nth_prime


@benchmark
def approach_2(nth: int) -> int:
    nth_prime = 0
    if nth == 2:
        nth_prime = 2
    nth -= 1
    for number_ in itertools.count(3, 1):
        if is_prime(number_):
            nth_prime = number_
            nth -= 1

        if nth == 0:
            break
    return nth_prime


print(normal(10001))
print(approach_2(10001))
