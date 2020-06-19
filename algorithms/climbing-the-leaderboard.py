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
    for score_alice in alice:
        rank = 1
        score_previous = -1
        for score_current in scores:
            if score_alice >= score_current:
                break
            if score_current != score_previous:
                rank += 1
            score_previous = score_current
        lb_ranks.append(rank)

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

