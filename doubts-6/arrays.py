import numpy

def arrays(arr):
    a=numpy.array(arr,float)
    return a[-1::-1]


arr = input().strip().split(' ')