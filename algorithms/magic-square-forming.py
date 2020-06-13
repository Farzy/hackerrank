#!/bin/python3

import itertools


def is_magic_square(square):
    s1 = sum(square[0:3])
    s2 = sum(square[3:6])
    s3 = sum(square[6:9])
    s4 = sum(square[0::3])
    s5 = sum(square[1::3])
    s6 = sum(square[2::3])
    s7 = sum(square[0::4])
    s8 = sum(square[2:7:2])

    return s1 == s2 == s3 == s4 == s5 == s6 == s7 == s8


def create_magic_squares_iter():
    return filter(is_magic_square, itertools.permutations(range(1, 10)))


def diff_squares(square_a, square_b):
    return sum(map(lambda item: abs(item[0] - item[1]), zip(square_a, square_b)))


# Complete the formingMagicSquare function below.
def forming_magic_square(square):
    min_sum = 999
    flat_s = tuple(x for row in square for x in row)

    for square in create_magic_squares_iter():
        min_sum = min(min_sum, diff_squares(flat_s, square))

    return min_sum


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = forming_magic_square(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    print(result)
