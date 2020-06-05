def minion_game(string):
    VOWELS = "AEIOU"
    total_len = len(string)
    stuart = 0
    for i in range(total_len):
        if string[i] not in VOWELS:
            stuart += total_len - i
    kevin = 0
    for i in range(total_len):
        if string[i] in VOWELS:
            kevin += total_len - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif stuart < kevin:
        print("Kevin", kevin)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
