#!/bin/python3
"""https://www.hackerrank.com/challenges/apple-and-orange/problem"""


# Complete the countApplesAndOranges function below.
def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apples_on_house = 0
    oranges_on_house = 0
    for apple in apples:
        if s <= a + apple <= t:
            apples_on_house += 1
    for orange in oranges:
        if s <= b + orange <= t:
            oranges_on_house += 1
    print(apples_on_house)
    print(oranges_on_house)


if __name__ == '__main__':
    s, t = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    m, n = list(map(int, input().split()))
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    count_apples_and_oranges(s, t, a, b, apples, oranges)
