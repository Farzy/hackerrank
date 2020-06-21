#!/bin/python3

import math


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    lcm = len(c) * k // math.gcd(len(c), k)
    return 100 - sum((c[i % len(c)] * 2 + 1) for i in range(0, lcm, k))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
