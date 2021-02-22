'''
Project Euler
Problem 4
2/14/2021

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]


def solution(n):
    upper_bound = 10 ** n - 1
    lower_bound = 10 ** (n - 1)

    return max(
        x * y
        for x in range(lower_bound, upper_bound + 1)
        for y in range(lower_bound, x + 1)
        if is_palindrome(x * y))


assert(solution(2) == 9009)
print(solution(3))
