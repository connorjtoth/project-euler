'''
Project Euler
Problem 40
3/21/2021

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
'''

from bisect import bisect_left
from utils import get_primes_by_sieve


def solution():
    possible_n = [n for n in range(1, 10)
                  if sum(i for i in range(1, n + 1)) % 3 != 0]

    max_candidate = sum((i + 1) * 10 ** i
                        for i in range(0, max(possible_n)))

    primes = list(get_primes_by_sieve(max_candidate))

    for n in reversed(possible_n):
        all_n_digits = {str(x) for x in range(1, n + 1)}
        low_prime_index = bisect_left(primes, 10 ** (n - 1))
        high_prime_index = bisect_left(primes, 10 ** n)
        for prime in reversed(primes[low_prime_index:high_prime_index]):
            if set(str(prime)) == all_n_digits:
                return prime


print(solution())
