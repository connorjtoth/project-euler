'''
Project Euler
Problem 1
2/14/2021

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def get_multiples(factors, upper_bound):
    return set.union(*(set(range(factor, upper_bound, factor)) for factor in factors))


def solution(upper_bound):
    return sum(get_multiples([3, 5], upper_bound))


assert(solution(10) == 23)
print(solution(1000))
