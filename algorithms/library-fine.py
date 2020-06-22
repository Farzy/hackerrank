#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import date, timedelta


# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    date1 = date(year=y1, month=m1, day=d1)
    date2 = date(year=y2, month=m2, day=d2)

    if date1 <= date2:
        return 0
    if (m1, y1) == (m2, y2):
        return (d2 - d1).days * 15
    else:
        return 42


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
