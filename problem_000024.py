'''
Project Euler
Problem 24
2/21/2021

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
'''

from math import factorial


def permute_n_times(permutation, n):
    num_terms = len(permutation)
    factorials = [factorial(x) for x in range(num_terms)]

    while n > 0:
        slot_index = max(index for index, value in enumerate(factorials)
                         if value <= n)
        slot_iterations = factorials[slot_index]
        term_index = n // slot_iterations
        term = permutation.pop(num_terms - slot_index - 1 + term_index)
        permutation.insert(num_terms - slot_index - 1, term)
        n -= slot_iterations * term_index

    return permutation


def solution(terms, iterations):
    first_permutation = list(sorted(terms))
    final_permutation = permute_n_times(first_permutation, iterations - 1)
    return ''.join(str(x) for x in final_permutation)


assert(solution({i for i in range(3)}, 6) == '210')
print(solution({i for i in range(10)}, 1000000))
