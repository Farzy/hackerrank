#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

#print(matrix)
m = [["{0:3}".format(row)[col] for row in matrix] for col in range(len(matrix[0]))]
flat_m = [item for sublist in m for item in sublist]
matrix = "".join(flat_m)
#print(matrix)
print(re.sub(r"(?<=[0-9a-zA-Z])[!@#$%& ]+(?=[0-9a-zA-Z])", " ", matrix))
