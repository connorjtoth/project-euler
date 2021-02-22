'''
Project Euler
Problem 14
2/20/2021

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


def collatz_length(n, memo={1: 1}):
    if n not in memo:
        terms = [n]

        while terms[-1] not in memo:
            terms.append(collatz(terms[-1]))

        base_length = memo[terms.pop()]
        num_terms = len(terms)
        memo.update({term: base_length + num_terms - i
                     for i, term in enumerate(terms)})
    return memo[n]


def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def solution(upper_bound, memo={1: 1}):
    _, best_start = max((collatz_length(n, memo), n)
                        for n in range(1, upper_bound))
    return best_start


assert(collatz_length(13) == 10)
print(solution(1000000))
