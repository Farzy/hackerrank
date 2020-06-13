#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    valley_cnt = 0
    current_height = 0

    for move in s:
        if move == 'D':
            current_height -= 1
            if current_height == -1:
                valley_cnt += 1
        elif move == 'U':
            current_height += 1

    return valley_cnt


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    print(result)
