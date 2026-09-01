'''
Project Euler
Problem 5
2/14/2021

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''

from math import lcm


def solution(n):
    return lcm(*range(1, n + 1))


assert(solution(10) == 2520)
print(solution(20))
