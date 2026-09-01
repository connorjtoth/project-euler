'''
Project Euler
Problem 36
2/27/2021

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
# '''

from itertools import chain, combinations
from math import log2


def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]


def binary_palindromes(upper_bound):
    palindromes = []
    max_digits = int(log2(upper_bound)) + 1
    for digits in range(max_digits):
        pairs = [{2 ** x, 2 ** (digits - x)}
                 for x in range(1, digits // 2 + 1)]

        combos = list(chain.from_iterable(
            (chain.from_iterable(combo)
             for combo in combinations(pairs, r))
            for r in range(len(pairs) + 1)))

        base = 2 ** digits + (digits > 0)
        palindromes.extend(base + sum(combo) for combo in combos)
    palindromes = filter(lambda x: x < upper_bound, palindromes)
    return palindromes


def solution(n):
    return sum(filter(is_palindrome, binary_palindromes(n)))



print(solution(1e6))

