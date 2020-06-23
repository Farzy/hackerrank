#!/bin/python3

import math


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0

    while c:
        try:
            first_1 = c.index(1)
            jumps += math.ceil((first_1 + 1) / 2)
            c = c[first_1 + 1:]
        except ValueError:
            jumps += math.ceil((len(c) - 1) / 2)
            c = []

    return jumps


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(result)
