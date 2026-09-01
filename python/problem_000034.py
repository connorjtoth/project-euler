'''
Project Euler
Problem 34
2/26/2021

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

from itertools import count
from math import factorial


def solution():
    factorial_sums = {x: factorial(x) for x in range(10)}
    upper_bound = next(10 ** i for i in count(1)
                       if 10 ** i > factorial_sums[9] * i)
    total = 0
    for n in range(10, upper_bound):
        value = factorial_sums[n // 10] + factorial_sums[n % 10]
        factorial_sums[n] = value
        if value == n:
            total += n
    return total


print(solution())
