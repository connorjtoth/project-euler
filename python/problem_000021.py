'''
Project Euler
Problem 21
2/20/2021

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from utils import get_divisors


def is_amicable_number(n, memo, primes):
    divisors = \
        get_divisors(n, memo, primes, proper=True)
    candidate_pair = sum(divisors)
    if n == candidate_pair:
        return False, 0
    candidate_divisors = \
        get_divisors(candidate_pair, memo, primes, proper=True)

    if n == sum(candidate_divisors):
        return True, candidate_pair
    else:
        return False, 0


def solution(upper_bound, memo={1: {1}}, primes=[2, 3]):
    amicable_numbers = set()
    for n in range(2, upper_bound):
        if n not in amicable_numbers:
            is_amicable, amicable_pair = is_amicable_number(n, memo, primes)
            if is_amicable:
                amicable_numbers |= {n, amicable_pair}
    return sum(amicable_numbers)


print(solution(10000))
