from itertools import groupby

s = input()
print(" ".join(map(lambda x: "({}, {})".format(len(list(x[1])), x[0]),
                   groupby(s))))
