'''
Project Euler
Problem 15
2/20/2021

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

    ___ ___         ___             ___
     X   X |         X |_X_          X | X
     X   X |         X   X |         X |_X_>
           V               V
    
   |_X___X_        |_X_  X         | X   X 
     X   X |         X |_X_>       |_X___X_>
           V


How many such routes are there through a 20×20 grid?
'''

from itertools import accumulate


def solution(rows, cols):
    paths = [1] * (cols + 1)
    for _ in range(rows):
        paths = accumulate(paths)
    return max(paths)


assert(solution(2, 2) == 6)
print(solution(20, 20))
