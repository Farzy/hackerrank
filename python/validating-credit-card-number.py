import re

for _ in range(int(input())):
    cc = input()
    if re.search(r"^[4-6]\d{3}(-?\d{4}){3}$", cc) and \
            not re.search(r"(.)(-?\1){3}", cc):
        print("Valid")
    else:
        print("Invalid")
