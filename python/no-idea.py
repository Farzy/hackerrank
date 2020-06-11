def happiness(arr, a, b):
    score = 0
    for n in arr:
        if n in a:
            score += 1
        elif n in b:
            score -= 1
    return score


if __name__ == '__main__':
    input()
    arr = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    result = happiness(arr, a, b)
    print(result)
