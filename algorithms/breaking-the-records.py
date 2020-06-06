#!/bin/python3
"""https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem"""

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breaking_records(scores):
    worst_score = best_score = scores[0]
    best_increased = worst_decreased = 0

    for score in scores[1:]:
        if score < worst_score:
            worst_score = score
            worst_decreased += 1
        elif score > best_score:
            best_score = score
            best_increased += 1

    return [best_increased, worst_decreased]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breaking_records(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
