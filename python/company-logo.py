from collections import Counter

c = Counter(list(input()))
common = c.most_common()
common.sort(key=lambda tup: -tup[1] * 256 + ord(tup[0]))
for tup in common[:3]:
    print(*tup)
