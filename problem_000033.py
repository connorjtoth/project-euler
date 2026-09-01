'''
Project Euler
Problem 33
2/26/2021

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''

from utils import get_divisors


def simplify_fraction(numerator, denominator, divisors_memo, primes_memo):
    num_divisors = get_divisors(numerator, divisors_memo, primes_memo)
    den_divisors = get_divisors(denominator, divisors_memo, primes_memo)
    fraction_divisors = num_divisors.intersection(den_divisors)
    if len(fraction_divisors) > 0:
        gcd = max(fraction_divisors)
        numerator //= gcd
        denominator //= gcd
    return numerator, denominator


def solution(divisors_memo={1: {1}}, primes_memo=[2, 3]):
    product_num = 1
    product_den = 1
    for numerator in (n for n in range(10, 100) if n % 10 != 0):
        num_digits = str(numerator)
        for denominator in (d for d in range(numerator + 1, 100)
                            if d % 10 != 0):
            den_digits = str(denominator)
            overlap = set(num_digits).intersection(den_digits)
            simplified = simplify_fraction(
                numerator, denominator, divisors_memo, primes_memo)

            if len(overlap) > 0 and simplified != (numerator, denominator):
                for overlap_value in overlap:
                    new_num = int(num_digits.replace(overlap_value, '', 1))
                    new_den = int(den_digits.replace(overlap_value, '', 1))
                    new_simplified = simplify_fraction(
                        new_num, new_den, divisors_memo, primes_memo)
                    if new_simplified == simplified:
                        product_num *= numerator
                        product_den *= denominator
    return simplify_fraction(
        product_num, product_den, divisors_memo, primes_memo)


print(solution())
