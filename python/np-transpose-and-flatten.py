import numpy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
narr = numpy.array(arr)
print(numpy.transpose(narr))
print(narr.flatten())
