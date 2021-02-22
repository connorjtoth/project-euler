'''
Project Euler
Problem 22
2/20/2021

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

NAMES_FILE = '.\\res\\p022_names.txt'
A_CODE = ord('A')


def alpha_value(word):
    return sum(ord(char) - A_CODE + 1 for char in word)


def solution():
    names = []
    with open(NAMES_FILE, 'r') as names_file:
        names.extend(x.strip('"') for x in names_file.readline().split(','))
    names.sort()
    return sum(alpha_value(name) * (index + 1)
               for index, name in enumerate(names))


print(solution())
