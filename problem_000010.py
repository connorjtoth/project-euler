'''
Project Euler
Problem 10
2/14/2021

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


def get_primes_by_sieve(n):
    sieve = [False, False, True] + [True] * n
    for candidate in range(2, int(n ** 0.5) + 1):
        if sieve[candidate]:
            for composite in range(candidate ** 2, n + 1, candidate):
                sieve[composite] = False
    return (x for x in range(n) if sieve[x])


def solution(n):
    return sum(get_primes_by_sieve(n))


assert(solution(10) == 17)
print(solution(2000000))
