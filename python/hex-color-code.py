import re

regex_pattern = r".(#[a-fA-F\d]{3}(?:[a-fA-F\d]{3})?)[,;)]"

n = int(input())
for _ in range(n):
    line = input()
    match = re.findall(regex_pattern, line)
    # print(line)
    if match:
        print("\n".join(match))
