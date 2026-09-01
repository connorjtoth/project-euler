'''
Project Euler
Problem 28
2/21/2021

Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

       _21_ 22  23  24  _25_
        20  _7_  8  _9_  10
        19   6  _1_  2   11
        18  _5_  4  _3_  12
       _17_ 16  15  14  _13_

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
'''


def solution(n):
    total = 1
    last_value = 1
    for ring_size in range(2, n, 2):
        for _ in range(4):
            last_value += ring_size
            total += last_value
    return total


assert(solution(5) == 101)
print(solution(1001))
