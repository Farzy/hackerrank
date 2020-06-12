import re

for _ in range(int(input())):
    uid = input()
    if re.search(r"^[0-9a-zA-Z]{10}$", uid) and \
            re.search(r"[A-Z].*[A-Z]", uid) and \
            re.search(r"[0-9].*[0-9].*[0-9]", uid) and \
            not re.search(r"(.).*\1", uid):
        print("Valid")
    else:
        print("Invalid")
