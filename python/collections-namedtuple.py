"""https://www.hackerrank.com/challenges/py-collections-namedtuple/problem"""

from collections import namedtuple
n = int(input()) ; Marks = namedtuple('Marks', ",".join(input().split())) ; sum = 0
for _ in range(n): mark = Marks(*input().split()) ; sum += int(mark.MARKS)
print("{0:.2f}".format(sum/n))
