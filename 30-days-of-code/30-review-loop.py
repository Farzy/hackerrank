"""https://www.hackerrank.com/challenges/30-review-loop/problem"""


def altern_print(word):
    odd_letters = ""
    for i, c in enumerate(word):
        if i % 2 == 0:
            print(c, end='')
        else:
            odd_letters += c
    print(" " + odd_letters)


if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        altern_print(input())
