"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is 385

The square of the sum of the first ten natural numbers is 3025,

Hence, the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
from util import benchmark


@benchmark
def normal(limit: int):
    sum_ = 0
    sum_of_squares_ = 0
    for i in range(limit + 1):
        sum_ += i
        sum_of_squares_ += i * i

    square_of_sum_ = sum_ * sum_
    return square_of_sum_ - sum_of_squares_


@benchmark
def progressions(limit: int) -> int:
    """
    sum of numbers can be calculated from AP sum formula
    Sn = (n/2)(2a+(n-1)*d)
    for natural numbers a = 1 and d = 1 substituting will give us
    S = (n * (n + 1)) / 2

    S^2 = [n * (n + 1) / 2]^2
    S^2 = (n^2 + n) * (n^2 + n) / 4
    S^2 = n^4 + 2n^3 + 5n^2 + 4n + 4

    sum of squares can be calculated from GP sum formula
    S = (n * (n + 1) * (2n + 1)) / 6

    S = 2n^3 + 3n^2 + n

    clearly square of sum is greater than sum of squares
    """

    sum_of_squares = (limit * (limit + 1) * (2 * limit + 1)) // 6
    n_sum = (limit * (limit + 1)) // 2
    square_of_sum = n_sum * n_sum

    return square_of_sum - sum_of_squares


print(normal(100))
print(progressions(100))
