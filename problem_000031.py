'''
Project Euler
Problem 31
2/24/2021

In the United Kingdom the currency is made up of pound (£) and pence (p).
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

PENCE_VALUES = [1, 2, 5, 10, 20, 50, 100, 200]


def solution(total, coins):
    memo = {(0, num_coins): 1 for num_coins in range(len(coins))}
    coins = sorted(coins)

    for goal in range(1, total + 1):
        for num_coins in range(len(coins) - 1, -1, -1):
            more_coins_value = memo.get((goal, num_coins + 1), 0)
            less_goal_value = memo.get((goal - coins[num_coins], num_coins), 0)
            memo[(goal, num_coins)] = more_coins_value + less_goal_value
    return memo[(total, 0)]


print(solution(200, PENCE_VALUES))
