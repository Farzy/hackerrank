PATTERN = ".|."

N, M = map(int, input().split())

for row in range(int((N-1) / 2)):
    print(("-" * int(M/2 - 3*row - 1)) + (PATTERN * (2 * row + 1)) + ("-" * int(M/2 - 3*row - 1)))
print(("-" * int((M-7)/2)) + "WELCOME" + ("-" * int((M-7)/2)))
for row in range(int((N-1) / 2) -1, -1, -1):
    print(("-" * int(M/2 - 3*row - 1)) + (PATTERN * (2 * row + 1)) + ("-" * int(M/2 - 3*row - 1)))
