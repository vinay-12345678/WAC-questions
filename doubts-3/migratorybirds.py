#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    list=[0,0,0,0,0,0]
    for i in arr:
        list[i]+=1

    ans=0
    maxbirds=0
    for i in range(1,6):
        if(list[i]>maxbirds):
            maxbirds=list[i]
            ans=i

    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
