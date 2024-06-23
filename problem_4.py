"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from util import benchmark


@benchmark
def normal(digits: int = 3) -> int:
    palindrome = 1
    count = 0
    i = (10 ** digits) - 1
    while i >= 10 ** (digits - 1):
        j = i
        while j >= 10 ** (digits - 1):
            count += 1
            prod = i * j
            if prod > palindrome and str(prod) == str(prod)[-1::-1]:
                palindrome = prod
            j -= 1
        i -= 1
    return palindrome


@benchmark
def optimized(digits: int = 3) -> int:
    a = (10 ** digits) - 1
    count = 0
    palindrome = 1
    while a >= 10 ** (digits - 1):
        rem = a % 11
        if rem == 0:
            b = a
            d = 1
        else:
            b = a - rem
            d = 11
        while b >= 10 ** (digits - 1):
            count += 1
            prod = a * b
            if prod > palindrome and str(prod) == str(prod)[-1::-1]:
                palindrome = prod
            b -= d
        a -= 1

    print(count)
    return palindrome


print(normal())
print(optimized())
