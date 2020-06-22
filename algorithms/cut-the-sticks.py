#!/bin/python3


# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    res = []
    while arr:
        res.append(len(arr))
        smallest = min(arr)
        arr = [a - smallest for a in arr if a - smallest]
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
    print(*result, sep='\n')
