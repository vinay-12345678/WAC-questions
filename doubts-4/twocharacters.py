#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    list=[0]*26
    #index=alphabet  0=a   1=b
    for i in s:
        list[ord(i)-ord('a')]+=1
    
    ans=0
    for i in range(0,26):
        if(list[i]>0):
            for j in range(i+1,26):
                if(list[j]>0):
                    st=""
                    # beabeefeab
                    for k in s:
                        if(ord(k)-ord('a')==i or ord(k)-ord('a')==j):
                            st+=k

                    flag=1
                    for k in range(0,len(st)-2):
                        if(st[k]!=st[k+2]):
                            flag=0
                            break

                    if(flag==1):
                        ans=max(len(st),ans)

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
