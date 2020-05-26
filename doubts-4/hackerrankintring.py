#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    st="hackerrank"
    index=0
    #haacckerrankkkkkkkk
    for i in s:
        if(index==len(st)):
            break
        
        if(i==st[index]):
            index+=1

    if(index==len(st)):
        return "YES"
    else:
        return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
