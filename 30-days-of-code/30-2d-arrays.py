#!/bin/python3


def hourglass_sum(arr, row, col):
    return sum(arr[row][col:col + 3]) + \
           arr[row + 1][col + 1] + \
           sum(arr[row + 2][col: col + 3])


def max_hourglass_sum(arr):
    max_sum = -999

    for row in range(len(arr) - 2):
        for col in range(len(arr[0]) - 2):
            max_sum = max(max_sum, hourglass_sum(arr, row, col))

    return max_sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(max_hourglass_sum(arr))
