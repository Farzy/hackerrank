#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    if len(w) == 1:
        return "no answer"
    for i in range(len(w)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if w[j] < w[i]:
                return "{}{}{}{}{}".format(w[0:j], w[i], w[j+1:i], w[j], w[i + 1:])
            # print("{}:{} {} {} {} {} {}".format(j, i, w[0:j], w[i], w[j+1:i], w[j], w[i + 1:]))
    return "no answer"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        # fptr.write(result + '\n')
        print(result)

    # fptr.close()
