#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ct = 0
    arrs = set(ar)
    ars = list(arrs)
    for i in range(len(ars)):
        nmb =ar.count(ars[i])
        if(nmb > 1):
            ct =ct+(nmb//2)
        else:
            continue 
    return ct
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
