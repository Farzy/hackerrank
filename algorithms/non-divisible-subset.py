#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # As found in the discussions (a+b) is divisible by k if
    # (a % k) + (b % k) is divisible by k. So let's start by counting
    # the elements in the array by the rest of their division by k
    modulos = [0] * k
    for i in s:
        modulos[i % k] += 1
    print("Modulos count:", modulos)
    # We now have k subsets.
    # We can combine subsets if:
    # * the indice is not 0 (because the sum of 2 members of modulos[0] is divisible by k)
    #   UNLESS we only include at most ONE number,
    # * the sum of their indices is not k,
    # * if k is even exclude index k/2 whose members sum is divisible by k
    # and mesure the size of these new subsets.
    # We cannot add a subset to itself.
    subsets_size = []
    for i in range(k - 1):
        for j in range(i +1, k):
            # Include subset alone, if indice is not zero and not half of k
            print((j,))
            if (k % 2 != 0) or (j != k // 2):
                subsets_size.append(modulos[j])
            # Test combinations of 2 subsets
            print((i, j), end='')
            if (i + j == k) or ((k % 2 == 0) and ((i == k // 2) or (j == k // 2))):
                print(": pass")
                pass
            elif i == 0:
                if modulos[0]:
                    print(": 1 (or 0 if empty list) + modulos({})".format(j))
                    subsets_size.append(1 + modulos[j])
                else:
                    print(": pass")
                    pass
            else:
                print(": modulos({}) + modulos({})".format(i, j))
                subsets_size.append(modulos[i] + modulos[j])

    print(subsets_size)
    return max(subsets_size)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(result)