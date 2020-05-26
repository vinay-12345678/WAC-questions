#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong

    lowercase=0
    uppercase=0
    digit=0
    special=0
    for i in password:
        if(i.islower()):
            lowercase=1
        elif(i.isupper()):
            uppercase=1
        elif(i.isdigit()):
            digit=1
        else:
            special=1

    ans=lowercase+uppercase+digit+special

    return max(6-n,4-ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
