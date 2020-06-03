#!/bin/python3
"""https://www.hackerrank.com/challenges/closest-numbers/problem"""

import math
import os
import random
import re
import sys


# Complete the closestNumbers function below.
def closestNumbers(arr):
    min_diff = float("inf")
    res = []
    arr.sort()
    for n in range(len(arr) - 1):
        diff = arr[n+1] - arr[n]
        if diff < min_diff:
            # New minimum diff
            min_diff = diff
            # Erase existing results
            res = arr[n:n+2]
        elif diff == min_diff:
            # Another minimum couple
            res.extend(arr[n:n+2])
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
