#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    arr.sort()
    ans=[]
    while(len(arr)>0):
        ans.append(len(arr))
        smallest=arr[0]
        for i in range(0,len(arr)):
            arr[i]=arr[i]-smallest

        while(len(arr)>0 and arr[0]==0):
            arr.pop(0)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
