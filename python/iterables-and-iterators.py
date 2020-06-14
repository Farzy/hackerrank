import itertools


if __name__ == '__main__':
    n = int(input())
    letter = input().split()
    k = int(input())

    combinations = tuple(itertools.combinations(letter, k))
    combinations_with_a = tuple(filter(lambda t: 'a' in t, combinations))

    print("{0:.3f}".format(len(combinations_with_a) / len(combinations)))
