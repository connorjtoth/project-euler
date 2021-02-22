'''
Project Euler
Problem 30
2/21/2021

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
'''

from itertools import count


def solution(powers, upper_bound=None):
    power_map = [x ** powers for x in range(10)]

    upper_bound = 10 ** next(n for n in count(1)
                             if int('9' * n) > n * power_map[9])

    return sum(candidate for candidate in range(10, upper_bound)
               if candidate == sum(power_map[d]
               for d in map(int, str(candidate))))


assert(solution(4) == 19316)
print(solution(5))
