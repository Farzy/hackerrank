"""https://www.hackerrank.com/challenges/defaultdict-tutorial/problem"""

from collections import defaultdict


def list_occurences(a, b):
    ad = defaultdict(list)
    for position, item in enumerate(a, 1):
        ad[item].append(position)
    for key in b:
        if key in ad.keys():
            print(" ".join(map(str, ad[key])))
        else:
            print("-1")


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    b = []
    # XXX Do not write "a = b = []" otherwise both variable will point to the same location!
    for _ in range(n):
        a.append(input())
    for _ in range(m):
        b.append(input())
    list_occurences(a, b)
