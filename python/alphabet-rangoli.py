import itertools


def print_rangoli(size):
    for n in itertools.chain(range(size-1, -1, -1), range(1, size)):
        pattern = "-".join(map(chr, itertools.chain(
            range(ord('a') + size - 1, ord('a') + n - 1, -1),
            range(ord('a') + n +1, ord('a') + size)
        )))
        print(pattern.center(4 * size - 3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
