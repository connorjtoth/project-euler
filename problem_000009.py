'''
Project Euler
Problem 9
2/14/2021

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from math import prod


def pythagorean_triples(n):
    triples = []
    for a in range(1, n // 3):
        a2 = a ** 2
        for b in range(a, n // 2):
            c = n - a - b
            if a2 + b ** 2 == c ** 2:
                triples.append((a, b, c))
    return triples


def solution(n):
    return prod(*pythagorean_triples(n))


assert(solution(3 + 4 + 5) == 3 * 4 * 5)
print(solution(1000))
