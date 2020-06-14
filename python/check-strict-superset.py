a = set(input().split())
n = int(input())

sets = []
for _ in range(n):
    sets.append(set(input().split()))

print(all(map(lambda s: s < a, sets)))
