from collections import deque

d = deque()

n = int(input())
for _ in range(n):
    verb, *args = input().split()
    if verb == "append":
        d.append(args[0])
    elif verb == "appendleft":
        d.appendleft(args[0])
    elif verb == "pop":
        d.pop()
    elif verb == "popleft":
        d.popleft()

print(*d)
