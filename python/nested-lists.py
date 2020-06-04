if __name__ == '__main__':
    arr = []
    min_score = float("inf")
    for _ in range(int(input())):
        name = input()
        score = float(input())
        min_score = min(min_score, score)
        arr.append([name, score])

    second_min_score = sorted([el[1] for el in arr if el[1] != min_score])[0]
    names = [el[0] for el in arr if el[1] == second_min_score]

    for name in sorted(names):
        print(name)
