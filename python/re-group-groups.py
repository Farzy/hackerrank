import re

s = input()
m = re.search(r'([0-9a-zA-Z])\1', s)
if m is not None:
    print(m.group(1))
else:
    print("-1")
