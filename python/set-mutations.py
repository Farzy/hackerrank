_ = input()
a = set(list(map(int, input().split())))
n = int(input())
for _ in range(n):
    op, length = input().split()
    b = set(list(map(int, input().split())))
    if op == "intersection_update":
        a &= b
    elif op == "difference_update":
        a -= b
    elif op == "symmetric_difference_update":
        a ^= b
    elif op == "update":
        a |= b

print(sum(a))
