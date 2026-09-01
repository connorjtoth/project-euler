'''
Project Euler
Problem 7
2/14/2021

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
'''


def get_n_primes(n):
    primes = [2, 3]
    if n < 2:
        return primes[:n]
    current = 3
    for i in range(2, n):
        while not all(current % p != 0 for p in primes):
            current += 2
        primes.append(current)
    return primes


def solution(n):
    return get_n_primes(n)[-1]


assert(solution(6) == 13)
print(solution(10001))
