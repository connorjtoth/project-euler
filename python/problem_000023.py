'''
Project Euler
Problem 23
2/20/2021

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
'''

from utils import get_divisors


def is_abundant(n, memo, primes):
    return n < sum(get_divisors(n, memo, primes, proper=True))


def solution(memo={1: {1}}, primes=[2, 3]):
    sum = 0
    abundants = set()

    for i in range(1, 28124):
        if not any((i - abundant) in abundants
                   for abundant in abundants):
            sum += i
        sum += i if not any((i - abundant) in abundants
                            for abundant in abundants) else 0
        if is_abundant(i, memo, primes):
            abundants.add(i)
    return sum


print(solution())