def symmetric_difference(m, n):
    m = set(m)
    n = set(n)
    res = list(m.difference(n))
    res.extend(list(n.difference(m)))
    res.sort()

    return res


if __name__ == '__main__':
    _, M = input(), list(map(int, input().split()))
    _, N = input(), list(map(int, input().split()))
    result = symmetric_difference(M, N)
    for n in result:
        print(n)

