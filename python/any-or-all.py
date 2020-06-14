_ = input() ; ints = list(map(int, input().split()))
print(all(map(lambda x: x>0, ints)) and
      any(map(lambda x: str(x) == "".join(list(reversed(str(x)))), ints)))
