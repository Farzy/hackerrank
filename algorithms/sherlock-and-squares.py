#!/bin/python3

import math
import os


# Complete the squares function below.
# Do not use a range to count the square roots because the list can be huge and
# calculation time explodes.
def squares(a, b):
    return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
