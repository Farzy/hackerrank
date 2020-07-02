#!/bin/python3


def max_bitwise_and(n, k):
    m = -1
    # find binary number of digits of k
    k_size = len(bin(k)) - 2  # Substract length of "0b"
    # build binary number of k_size, maxed by "n"
    kk = min(n, int("1" * k_size, 2))
    # We know that a&b cannot be > kk
    for a in range(1, kk):
        for b in range(a + 1, kk + 1):
            a_and_b = a & b
            if m < a_and_b < k:
                m = a_and_b
    return m


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(max_bitwise_and(n, k))
