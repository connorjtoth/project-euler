'''
Project Euler
Problem 17
2/20/2021

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
'''


from math import log10

DIGIT_DEFINITIONS = [
    ('zero', ''),
    ('one', ''),
    ('two', 'twen'),
    ('three', 'thir'),
    ('four', 'for'),
    ('five', 'fif'),
    ('six', 'six'),
    ('seven', 'seven'),
    ('eight', 'eigh'),
    ('nine', 'nine'),
]
DIGITS, DIGIT_PREFIXES = zip(*DIGIT_DEFINITIONS)
BASES = [
    'one',
    'ten',
    'hundred',
    'thousand',
]
SPECIAL_NUMBERS = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    14: 'fourteen',
}


def written_out_number(n):
    result = ''
    if n < 100:
        if n in SPECIAL_NUMBERS:
            result = SPECIAL_NUMBERS[n]
        elif n % 10 == 0:
            result = DIGIT_PREFIXES[n // 10] + 'ty'
        elif n < 10:
            result = DIGITS[n]
        elif n < 20:
            result = DIGIT_PREFIXES[n % 10] + 'teen'
        else:
            result = written_out_number(n - n % 10)
            if n % 10 != 0:
                result += DIGITS[n % 10]
    else:
        places = int(log10(n))
        base = 10 ** places
        result = DIGITS[n // base] + BASES[places]
        if 0 < n % base < 100:
            result += 'and' + written_out_number(n % base)
    return result


def solution(n):
    return len(''.join(written_out_number(x) for x in range(1, n + 1)))


assert(solution(5) == 19)
print(solution(1000))
