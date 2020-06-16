import re

n = int(input())
for _ in range(n):
    s = input()
    if re.search(r'^[+-]?\d*\.\d+$', s):
        try:
            x = float(s)
            print(True)
        except ValueError:
            print(False)
    else:
        print(False)
