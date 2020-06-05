n = int(input())
words = {}
for _ in range(n):
    word = input()
    words[word] = words.setdefault(word, 0) + 1

print(len(words))
print(*words.values())
