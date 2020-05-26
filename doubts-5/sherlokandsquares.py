#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    lower=math.ceil(a**0.5)
    upper=b**0.5

    ans=0
    while(lower<=upper):
        ans+=1
        lower+=1

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
