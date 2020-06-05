def merge_the_tools(string, k):
    n = len(string)
    for i in range(int(n/k)):
        t = string[k * i:k * (i + 1)]
        u = ""
        for c in t:
            if not c in u:
                u += c
        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
