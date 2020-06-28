#!/bin/python3

from functools import reduce
from operator import add


# Complete the organizingContainers function below.
def organizingContainers(container):
    container_count = len(container)
    # Find total number of balls of type (n) for each container (n)
    ball_count = [reduce(add, [container[i][j] for i in range(container_count)], 0)
                  for j in range(container_count)]
    ball_count.sort()
    # Find total volume of each container
    container_size = [sum(container[i]) for i in range(container_count)]
    container_size.sort()
    if ball_count == container_size:
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        # fptr.write(result + '\n')
        print(result)

    # fptr.close()
