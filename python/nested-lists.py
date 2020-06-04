if __name__ == '__main__':
    arr = []
    min_score = float("inf")
    second_min_score = float("inf")
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < min_score:
            second_min_score = min_score
            min_score = score
        elif min_score < score < second_min_score:
            second_min_score = score
        arr.append([name, score])

    names = [el[0] for el in arr if el[1] == second_min_score]

    for name in sorted(names):
        print(name)
