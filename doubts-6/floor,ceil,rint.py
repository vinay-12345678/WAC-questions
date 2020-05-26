import numpy

numpy.set_printoptions(sign=' ')

a=[float(i) for i in input().strip().split()]

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))

