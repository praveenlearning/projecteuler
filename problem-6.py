"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is 385

The square of the sum of the first ten natural numbers is 3025,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
                                            3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of
            the sum.
"""

n = 100

n_sum = (n * (n + 1)) // 2
square_of_sum = n_sum * n_sum

sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6

# S1
# (n2 + n + 2)*(n2 + n + 2)
# n4 + 2n3 + 5n2 + 4n + 4

# S2
# (n * (n + 1) * (2 * n + 1)) // 6
# (2n3 + n2 + 2n2 + n) // 6


# S1 > S2

print(square_of_sum - sum_of_squares)
