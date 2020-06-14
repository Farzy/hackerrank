import re


def wrapper(f):
    def fun(l):
        nums = list(map(lambda m: re.sub(r'^(\+?91|0)?(.{5})(.{5})', r'+91 \2 \3', m), l))
        return f(nums)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
