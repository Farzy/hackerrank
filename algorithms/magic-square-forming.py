#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


def is_magic_square(s):
    # print("Is {} magic?".format(s))
    s1 = sum(s[0:3])
    s2 = sum(s[3:6])
    s3 = sum(s[6:9])
    s4 = sum(s[i] for i in [0, 3, 6])
    s5 = sum(s[i] for i in [1, 4, 7])
    s6 = sum(s[i] for i in [2, 5, 8])
    s7 = sum(s[i] for i in [0, 4, 8])
    s8 = sum(s[i] for i in [2, 4, 6])

    return s1 == s2 == s3 == s4 == s5 == s6 == s7 == s8


def create_magic_squares_iter():
    return filter(is_magic_square, itertools.permutations(range(1, 10)))


def diff_squares(square_a, square_b):
    return sum(map(lambda item: abs(item[0] - item[1]), zip(square_a, square_b)))


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    min_sum = 999
    flat_s = tuple(x for row in s for x in row)

    for square in create_magic_squares_iter():
        min_sum = min(min_sum, diff_squares(flat_s, square))

    return min_sum


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    print(result)
