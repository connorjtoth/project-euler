'''
Project Euler
Problem 19
2/20/2021

You are given the following information, but you may prefer to do some
research for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
'''

NORMAL_DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_DAYS_IN_MONTH = NORMAL_DAYS_IN_MONTH
LEAP_DAYS_IN_MONTH[1] = 29
FIRST_SUNDAY_YEAR = 1990
FIRST_SUNDAY_DATE = 2


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False


def days_in_year(year):
    return sum(NORMAL_DAYS_IN_MONTH) \
        if is_leap_year(year) else sum(LEAP_DAYS_IN_MONTH)


def first_sunday_in_year(year):
    first_sunday = FIRST_SUNDAY_DATE
    for year in range(FIRST_SUNDAY_YEAR, year):
        first_sunday = (days_in_year(year) - first_sunday) % 7
    return first_sunday


def solution(start, end):
    count = 0
    first_sunday = first_sunday_in_year(start)

    for year in range(start, end):
        days_in_month = NORMAL_DAYS_IN_MONTH \
                if is_leap_year(year) else LEAP_DAYS_IN_MONTH

        for month in range(len(days_in_month)):
            count += first_sunday == 0
            first_sunday = (days_in_month[month] + first_sunday) % 7
    return count


print(solution(1901, 2001))
