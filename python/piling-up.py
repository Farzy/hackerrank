def pile(n, cubes):
    pile = [float("inf")]
    while len(cubes):
        if cubes[0] > cubes [-1]:
            cube = cubes[0]
            del cubes[0]
        else:
            cube = cubes[-1]
            del cubes[-1]
        # Now type piling the cube
        if cube <= pile[-1]:
            pile.append(cube)
        else:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        n = int(input())
        cubes = list(map(int, input().split()))
        pile(n, cubes)
