import numpy as np

m, n = map(int, input().split())

y = []
features = []
for _ in range(n):
    *feature, single_y = map(float, input().split())
    f = [1.0]
    f.extend(feature)
    features.append(f)
    y.append(single_y)

features = np.array(features)
y = np.array(y)

queries = []
q = int(input())
for _ in range(q):
    query = list(map(float, input().split()))
    f = [1.0]
    f.extend(query)
    queries.append(np.array(f))

features_t = features.transpose()

b = np.linalg.inv(features_t.dot(features)).dot(features_t).dot(y)

for query in queries:
    res = query.dot(b)
    print("{:.2f}".format(res))
