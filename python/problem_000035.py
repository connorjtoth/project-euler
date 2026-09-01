'''
Project Euler
Problem 35
2/27/2021

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
'''

from math import log10
from utils import get_primes_by_sieve


def rotate_number(n):
    rotator = n
    digits = int(log10(n))
    while True:
        yield rotator
        first_digit = rotator // (10 ** digits)
        rotator = rotator * 10 + first_digit
        rotator %= (10 ** (digits + 1))
        if rotator == n:
            break


def solution(upper_bound):
    primes = set(get_primes_by_sieve(upper_bound))
    circular_primes = [2, 5]

    for prime in primes:
        if prime not in circular_primes:
            circular_primes.extend(
                x for x in rotate_number(prime)
                if not any(d in '024568' for d in str(prime))
                and all(c in primes for c in rotate_number(prime)))
    return len(circular_primes)


assert(solution(100) == 13)
print(solution(10 ** 6))