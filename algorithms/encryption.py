#!/bin/python3

import math
import re
from itertools import zip_longest


def matrix_size(text_size):
    row = col = math.floor(math.sqrt(text_size))
    # Adjust matrix size while keeping row < col
    if row * col < text_size:
        col += 1
        if row * col < text_size:
            row += 1
    return row, col


# Complete the encryption function below.
def encryption(s):
    row, col = matrix_size(len(s))
    # Split string in substring of "col" characters
    matrix = list(filter(None, re.split("(" + ("." * col) + ")", s)))
    # Join letters vertically
    words = ' '.join(map(lambda x: ''.join(x), zip_longest(*matrix, fillvalue='')))

    return words


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    # fptr.write(result + '\n')

    # fptr.close()
    print(result)
