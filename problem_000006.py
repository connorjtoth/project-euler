'''
Project Euler
Problem 6
2/14/2021

The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is

    3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''


def solution(n):
    sum_of_squares = sum(x ** 2 for x in range(1, n + 1))
    square_of_sums = sum(range(1, n + 1)) ** 2
    return square_of_sums - sum_of_squares


assert(solution(10) == 2640)
print(solution(100))
