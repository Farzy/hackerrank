#!/bin/python3


# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    def is_kaprekar(num):
        num_len = len(str(num))
        s = str(num * num)
        try:
            left = int(s[:-num_len])
        except ValueError:
            left = 0
        right = int(s[-num_len:])
        return left + right == num

    output = " ".join(map(str, filter(is_kaprekar, range(p, q + 1))))
    if output == "":
        output = "INVALID RANGE"
    print(output)


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
