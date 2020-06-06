#!/bin/python3

import os


# Complete the divisibleSumPairs function below.
def divisible_sum_pairs(n, k, ar):
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisible_sum_pairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
