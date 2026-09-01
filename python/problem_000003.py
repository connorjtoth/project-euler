'''
Project Euler
Problem 3
2/14/2021

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


def prime_factors(n):
    primes, prime_factors = [], []
    i = 2
    while i <= n:
        if all(i % p != 0 for p in primes):
            primes.append(i)
            while n % i == 0:
                prime_factors.append(i)
                n /= i
        i += 2 if i % 2 != 0 else 1
    return prime_factors


def solution(n):
    return max(prime_factors(n))


assert(solution(13195) == 29)
print(solution(600851475143))
