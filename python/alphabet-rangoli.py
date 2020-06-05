import itertools
from string import ascii_lowercase

def print_rangoli(size):
    for n in itertools.chain(range(size-1, -1, -1), range(1, size)):
        s = ascii_lowercase[n:size]
        s2 = s[::-1]
        pattern = "-".join(s2 + s[1:])
        print(pattern.center(4 * size - 3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
