import numpy
import pprint

n = int(input())

a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

b = []
for _ in range(n):
    b.append(list(map(int,input().split())))

# Transpose b
b = [[row[col] for row in b] for col in range(len(b[0]))]

p = []
for row in range(n):
    new_row = []
    for col in range(n):
        new_row.append(numpy.dot(a[row], b[col]))
    p.append(new_row)

p =numpy.array(p)
print(p)
