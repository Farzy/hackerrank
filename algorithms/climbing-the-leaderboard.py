#!/bin/python3

from itertools import groupby


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    lb_ranks = []
    scores_unique = list(map(lambda x: x[0], groupby(scores)))
    rank = len(scores_unique)
    for score_alice in alice:
        while True:
            if rank == 0 or score_alice < scores_unique[rank - 1]:
                lb_ranks.append(rank + 1)
                break
            if score_alice == scores_unique[rank - 1]:
                lb_ranks.append(rank)
                break
            rank -= 1

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
