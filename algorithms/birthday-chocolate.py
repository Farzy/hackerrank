#!/bin/python3

import os


# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    for start in range(len(s) - m + 1):
        if sum(s[start:start+m]) == d:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
