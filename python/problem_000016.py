'''
Project Euler
Problem 16
2/20/2021

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''


def solution(n):
    return sum(int(digit) for digit in str(2 ** n))


assert(solution(15) == 26)
print(solution(1000))
