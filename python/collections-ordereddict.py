from collections import OrderedDict

n = int(input())
d = OrderedDict()
for _ in range(n):
    k, v = input().rsplit(maxsplit=1)
    if k in d:
        d[k] += int(v)
    else:
        d[k] = int(v)

for k in d:
    print(k, d[k])
