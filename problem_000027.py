'''
Project Euler
Problem 27
2/21/2021

Euler discovered the remarkable quadratic formula:

    n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0 <= n <= 39. However, when n = 40,
40^2 + 40 + 41 = 40 *(40 + 1) + 41 is divisible by 41, and certainly
when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
primes for the consecutive values 0 <= n <= 79. The product of the
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
'''


def parity(n):
    return (n + 1) % 2


def is_prime(n, primes):
    if n not in primes:
        i = primes[-1] + 2
        while i <= n:
            if all(i % p != 0 for p in primes):
                primes.append(i)
            i += 2
    return n in primes


def prime_sequence_length(a, b, primes):
    n = 0
    while is_prime(n * (n + a) + b, primes):
        n += 1
    return n, a, b


def solution(upper_bound, primes=[2, 3]):
    best = (0, 0, 0)
    upper_bound -= parity(upper_bound)
    lower_bound = -upper_bound
    for a in range(lower_bound + 2, upper_bound - 2, 2):
        for b in range(best[0] - parity(best[0]), upper_bound + 1, 2):
            pos = prime_sequence_length(a, b, primes)
            neg = prime_sequence_length(a, -b, primes)
            best = max(pos, neg, best)
    return best


print(solution(1000))