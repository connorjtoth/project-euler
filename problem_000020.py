'''
Project Euler
Problem 20
2/20/2021

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

from math import prod


def solution(n):
    return sum(int(x) for x in str(prod(range(1, n + 1))))


print(solution(10))
assert(solution(10) == 27)
print(solution(100))
