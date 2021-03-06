import numpy

numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
a = numpy.array([list(map(int, input().split())) for _ in range(n)])
print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))
print(numpy.std(a))
