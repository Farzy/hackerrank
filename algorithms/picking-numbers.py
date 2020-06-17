#!/bin/python3


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    counts = {}
    for k in a:
        counts[k] = counts.get(k, 0) + 1

    res = max(counts[x] + counts.get(x + 1, 0) for x in counts.keys())
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    print(result)
