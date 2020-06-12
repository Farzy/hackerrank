import re


def and_or(match):
    if match.group(1)[0] == '&':
        return " and"
    else:
        return " or"


n = int(input())
for _ in range(n):
    line = input()
    print(re.sub(r' (&&|\|\|)(?=\s)', and_or, line))
