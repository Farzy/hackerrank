n, x = map(int, input().split())

marks = []
for _ in range(x):
    marks.append(list(map(float, input().split())))

avg = map(lambda m: sum(m) / x, zip(*marks))

for a in avg:
    print("{:.1f}".format(a))
