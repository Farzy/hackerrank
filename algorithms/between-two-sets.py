#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    numbers_between = range(a[-1], b[0]+1)

    def is_multiple_of_a(n):
        for i in a:
            if n % i != 0:
                return False
        return True

    def is_factor_of_b(n):
        for i in b:
            if i % n != 0:
                return False
        return True

    numbers_between = list(filter(is_multiple_of_a, numbers_between))
    numbers_between = list(filter(is_factor_of_b, numbers_between))
    return len(numbers_between)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
