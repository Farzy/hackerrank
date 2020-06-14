cube = lambda x: x ** 3


def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        f = fibonacci(n-1)
        new = f[-2] + f[-1]
        f.append(new)
        return f


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
