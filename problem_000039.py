'''
Project Euler
Problem 39
3/14/2021

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

from operator import itemgetter
from utils import get_divisors, get_primes_by_sieve


def coprime(a, b, divisors, primes):
    a_divisors = get_divisors(a, divisors, primes, True) - {1}
    b_divisors = get_divisors(b, divisors, primes, True) - {1}
    return a_divisors.isdisjoint(b_divisors)


def solution(upper_bound):
    primes = list(get_primes_by_sieve(upper_bound))
    divisors = {1: {1}}
    triples_by_perimeters = {}
    for m in range(3, upper_bound + 1, 2):
        for n in range(1, upper_bound // m - m + 1, 2):
            if coprime(m, n, divisors, primes):
                p = m * n + m * m
                triples_by_perimeters[p] = triples_by_perimeters.get(p, 0) + 1
    return max(triples_by_perimeters.items(), key=itemgetter(1))[0]


print(solution(1000))
