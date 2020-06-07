#!/bin/python3
"""https://www.hackerrank.com/challenges/migratory-birds/problem"""

from collections import defaultdict


# Complete the migratoryBirds function below.
def migratory_birds(arr):
    max_birds = 0
    bird_count = defaultdict(int)
    for bird in arr:
        bird_count[bird] += 1
        max_birds = max(max_birds, bird_count[bird])
    return sorted(filter(lambda item: bird_count[item] == max_birds, bird_count.keys()))[0]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratory_birds(arr)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
