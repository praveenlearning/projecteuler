"""
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
even-valued terms.


F(n) = F(n+1) - F(n-1)
F(n-1) = F(n) - F(n - 2)
F(n-2) = F(n-1) - F(n - 3)
...
...
F(4) = F(5) - F(3)
F(3) = F(4) - F(2)
F(2) = F(3) - F(1)

F(2) + ... + F(n) = F(n+1) + F(n) - F(2) - F(1)
F(1) + ... + F(n) = F(n+2) - F(2)
"""
from util import benchmark

limit = 4_000_000


@benchmark
def normal(n: int) -> int:
    f1 = 1
    f2 = 2
    sum_n = 0
    while f2 < n:
        if f2 % 2 == 0:
            sum_n += f2
        f1, f2 = f2, f1 + f2
    return sum_n


@benchmark
def optimized(n: int):
    """
    F= 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
    every 3rd term is even

    F(n)    = F(n-1) + F(n-2)
            = F(n-2) + F(n-3) + F(n-2) = 2 * F(n-2) + F(n-3)
            = 2 * (F(n-3) + F(n-4)) + F(n-3) = 3 * F(n-3) + 2 F(n-4)
            = 3 F(n-3) + F(n-4) + F(n-5) + F(n-6)
            = 4 F(n-3) + F(n-6)

    E(n)    = 4 E(n-1) + E(n-2) ----- Even Fibonacci Formula
    """
    e0 = 0
    e1 = 2
    sum_n = 0
    while e1 < n:
        sum_n += e1
        e0, e1 = e1, 4 * e1 + e0
    return sum_n


print(normal(limit))
print(optimized(limit))
