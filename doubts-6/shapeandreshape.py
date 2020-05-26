import numpy

a=[int(i) for i in input().strip().split()]
a=numpy.array(a)

print (a.reshape(3,3))
