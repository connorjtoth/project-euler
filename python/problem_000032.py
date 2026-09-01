'''
Project Euler
Problem 32
2/26/2021

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''
from math import log10

def get_pandigital_products(n):
    products = set()
    max_digits = (n - 1) // 2
    upper_bound = 10 ** max_digits
    all_digits = {str(x) for x in range(1, n + 1)}

    for multiplicand in range(1, int(upper_bound ** 0.5)):
        lower_bound = 10 ** int(max_digits - log10(multiplicand + 1))
        for multiplier in range(lower_bound, upper_bound // multiplicand):
            product = multiplicand * multiplier
            candidate = str(multiplicand) + str(multiplier) + str(product)
            if set(candidate) == all_digits:
                products.add(product)
    return products


def solution(n):
    return sum(get_pandigital_products(n))


print(solution(9))
