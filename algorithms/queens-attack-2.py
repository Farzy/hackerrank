#!/bin/python3


DIRECTION = {
    'N': (1, 0),
    'NE': (1, 1),
    'E': (0, 1),
    'SE': (-1, 1),
    'S': (-1, 0),
    'SW': (-1, -1),
    'W': (0, -1),
    'NW': (1, -1),
}


def in_bounds(n, rq, cq):
    return 1 <= rq <= n and 1 <= cq <= n


def explore_direction(n, rq, cq, obstacles, direction):
    r_inc, c_inc = DIRECTION[direction]
    count = 0
    rq += r_inc
    cq += c_inc
    while in_bounds(n, rq, cq) and [rq, cq] not in obstacles:
        count += 1
        rq += r_inc
        cq += c_inc
    return count


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    count = 0
    for direction in DIRECTION.keys():
        count += explore_direction(n, r_q, c_q, obstacles, direction)
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(result)
