import re

regex_pattern = r"<[a-zA-Z][\w._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>"

n = int(input())
for _ in range(n):
    email = input()
    if re.search(regex_pattern, email):
        print(email)
