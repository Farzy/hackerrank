#!/bin/python3


#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#
def taum_bday(b, w, bc, wc, z):
    if bc == wc:
        return b * bc + w * wc
    elif bc < wc and z < abs(bc - wc):
        return (b + w) * bc + w * z
    elif bc > wc and z < abs(bc - wc):
        return (b + w) * wc + b * z
    else:
        return b * bc + w * wc


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taum_bday(b, w, bc, wc, z)

        # fptr.write(str(result) + '\n')
        print(result)

    # fptr.close()
