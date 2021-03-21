'''
Project Euler
Problem 37
2/27/2021

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime at
each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

from utils import get_primes_by_sieve
from math import log10


def is_prime(n, primes):
    if n not in primes:
        i = max(primes) + 2
        while i <= n:
            if all(i % p != 0 for p in primes):
                primes.add(i)
            i += 2
    return n in primes


def is_ltp(candidate, primes, ltps):
    if candidate not in ltps:
        candidates = []
        for digits in range(int(log10(candidate)), -1, -1):
            if not is_prime(candidate, primes):
                return False
            candidates.append(candidate)
            candidate %= 10 ** digits
            if candidate in ltps:
                break
        ltps.extend(candidates)
    return True


def solution():
    primes = set(get_primes_by_sieve(int(1e6)))
    rtps, ltps, truncatable_primes = [], [], []
    new_rtps = [2, 3, 5, 7]

    while len(truncatable_primes) < 11:
        rtp_candidates = [rtp * 10 + i
                          for rtp in new_rtps
                          for i in {1, 3, 7, 9}]
        new_rtps = [candidate
                    for candidate in rtp_candidates
                    if is_prime(candidate, primes)]
        rtps.extend(new_rtps)
        for rtp in new_rtps:
            if is_ltp(rtp, primes, ltps):
                truncatable_primes.append(rtp)
    return sum(truncatable_primes)


print(solution())