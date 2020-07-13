import numpy as np

m, n = map(int, input().split())

y = []
features = []
for _ in range(n):
    *feature, single_y = map(float, input().split())
    features.append([1.0] + feature)
    y.append(single_y)

features = np.array(features)
y = np.array(y)

queries = []
q = int(input())
for _ in range(q):
    query = list(map(float, input().split()))
    queries.append(np.array([1.0] + query))

features_t = features.transpose()

b = np.linalg.inv(features_t.dot(features)).dot(features_t).dot(y)

for query in queries:
    res = query.dot(b)
    print("{:.2f}".format(res))
