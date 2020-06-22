#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    n = 0
    len_s = len(s)
    len_t = len(t)
    while n < min(len_s, len_t) and s[n] == t[n]:
        n += 1
    if k > (len(t) - n) and len(s) + len(t) - 2 * n <= k:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
