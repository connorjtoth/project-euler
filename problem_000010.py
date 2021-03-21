'''
Project Euler
Problem 10
2/14/2021

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from utils import get_primes_by_sieve


def solution(n):
    return sum(get_primes_by_sieve(n))


assert(solution(10) == 17)
print(solution(2000000))
