#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    if len(w) == 1:
        return "no answer"
    p = permutations(w)
    ww = None
    for s in p:
        new_w = ''.join(s)
        if new_w > w:
            if ww is None:
                ww = new_w
            else:
                ww = min(ww, new_w)
    if ww:
        return ww
    else:
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
