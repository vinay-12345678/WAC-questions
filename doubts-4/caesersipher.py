#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    # middle-Outz
    ans=""
    for i in s:
        if(i.isalpha()):
            if(i.islower()):
                ans+=chr(97+((ord(i)-ord('a'))+k)%26)

            elif(i.isupper()):
                ans+=chr(65+((ord(i)-ord('A'))+k)%26)

        else:
            ans+=i

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
