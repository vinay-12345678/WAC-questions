import numpy
value=input().split()
n=int(value[0])
m=int(value[1])
a=[]
for i in range(n):
    list=[int(i) for i in input().strip().split()]
    a.append(list)

a=numpy.array(a)

print(a.transpose())
print(a.flatten())

