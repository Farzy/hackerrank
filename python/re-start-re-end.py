import re

s = input()
reg = re.compile(input())
pos = 0
found_once = False

while True:
    m = reg.search(s, pos)
    if m:
        print("({}, {})".format(m.start(), m.end() - 1))
        pos = m.start() + 1
        found_once = True
    else:
        break
if not found_once:
    print((-1, -1))
