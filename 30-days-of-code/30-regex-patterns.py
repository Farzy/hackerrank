#!/bin/python3

import re


if __name__ == '__main__':
    N = int(input())

    names = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if re.search(r"^[a-z.]+@gmail.com$", emailID):
            names.append(firstName)

    print('\n'.join(sorted(names)))
