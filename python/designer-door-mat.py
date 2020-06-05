PATTERN = ".|."

N, M = map(int, input().split())

for row in range(int((N-1) / 2)):
    print((PATTERN * (2 * row + 1)).center(M, '-'))
print("WELCOME".center(M, "-"))
for row in range(int((N-1) / 2) -1, -1, -1):
    print((PATTERN * (2 * row + 1)).center(M, '-'))
