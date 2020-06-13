#!/bin/python3

import os
import sys


#
# Complete the pageCount function below.
#
def pageCount(n, p):
    from_front = p // 2
    from_back = (n - p) // 2
    if n % 2 == 0 and p == n - 1:
        from_back += 1

    return min(from_front, from_back)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    print(result)
