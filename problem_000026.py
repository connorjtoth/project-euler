'''
Project Euler
Problem 26
2/21/2021

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
'''


def unit_fraction_decimal(n):
    decimal = []
    patterns = {}
    dividend = 1
    divisor = n

    while dividend > 0:
        dividend *= 10
        quotient, dividend = dividend // divisor, dividend % divisor
        if (dividend, divisor) in patterns:
            return len(decimal) - patterns[(dividend, divisor)], n, decimal
        else:
            decimal += [quotient]
            patterns[(dividend, divisor)] = len(decimal) - 1
    return 0, n, decimal


def solution(upper_bound):
    _, denom, _ = max(unit_fraction_decimal(denom)
                      for denom in range(2, upper_bound))
    return denom


assert(solution(10) == 7)
print(solution(1000))
