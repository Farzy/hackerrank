import itertools
import math


def f(tup, modulo):
    return sum(map(lambda x: x*x, tup)) % modulo


if __name__ == '__main__':
    k, m = map(int, input().split())
    k_list = []
    for _ in range(k):
        k_list.append(tuple(map(int, input().split()[1:])))

    max_f = -math.inf
    for t in itertools.product(*k_list):
        result = f(t, modulo=m)
        max_f = max(max_f, result)

    print(max_f)
