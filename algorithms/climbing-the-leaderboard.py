#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    lb_ranks = []
    for score in alice:
        scores_new = scores[:]
        scores_new.append(score)
        scores_new.sort(key=lambda x: -x)
        alice_rank = list(map(lambda x: x[0],
                              groupby(scores_new))).index(score) + 1
        lb_ranks.append(alice_rank)

    return lb_ranks


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print('\n'.join(map(str, result)))
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

