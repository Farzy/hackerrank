import itertools


sorting_keys = "".join(list(itertools.chain(
    map(chr,range(ord('a'), ord('z') + 1)),
    map(chr,range(ord('A'), ord('Z') + 1)),
    map(str, range(1, 10, 2)),
    map(str, range(0, 10, 2)),
)))


if __name__ == '__main__':
    s = input()
    s_sorted = "".join(sorted(iter(s), key=lambda x: sorting_keys.index(x)))
    print(s_sorted)
