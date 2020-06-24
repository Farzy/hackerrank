#!/bin/python3

from collections import Counter


# Complete the equalizeArray function below.
def equalizeArray(arr):
    c = Counter(arr)
    common_count = c.most_common(1)[0][1]
    return len(arr) - common_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(result)
