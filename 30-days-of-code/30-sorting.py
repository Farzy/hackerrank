#!/bin/python3


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
global_numswaps = 0
for i in range(n):
    local_numswaps = 0

    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            local_numswaps += 1

    global_numswaps += local_numswaps
    if not local_numswaps:
        break

print("Array is sorted in", global_numswaps, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[-1])
