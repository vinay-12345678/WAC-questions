#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level=0
    valley=0
    ans=0
    for i in s:
        if(i=='U'):
            level+=1
        
        elif(i=='D'):
            level-=1

        if(level<0):
            valley=1
        
        elif(level==0 and valley==1):
            ans+=1
            valley=0

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
