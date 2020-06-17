class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        elts_sorted = sorted(self.__elements)
        self.maximumDifference = elts_sorted[-1] - elts_sorted[0]


# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
