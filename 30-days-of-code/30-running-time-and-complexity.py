import itertools
import math


def is_prime(num):
    if num == 2:
        return "Prime"
    elif num == 1 or num % 2 == 0:
        return "Not prime"
    else:
        n_sqrt = math.sqrt(num)
        divisor = 3
        increment = itertools.chain([2, 2, 4], itertools.cycle([2, 4, 2, 4, 6, 2, 6, 4]))
        while divisor <= n_sqrt:
            if num % divisor == 0:
                return "Not prime"
            divisor += next(increment)
        return "Prime"


if __name__ == '__main__':
    n = int(input())
    for i in [int(input()) for _ in range(n)]:
        print(is_prime(i))
