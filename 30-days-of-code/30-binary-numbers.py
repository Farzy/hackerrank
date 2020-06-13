#!/bin/python3


if __name__ == '__main__':
    n = int(input())
    max_ones = 0
    current_ones = 0

    while n != 0:
        if n % 2 == 1:
            current_ones += 1
        else:
            current_ones = 0
        n //= 2
        max_ones = max(max_ones, current_ones)

    print(max_ones)
