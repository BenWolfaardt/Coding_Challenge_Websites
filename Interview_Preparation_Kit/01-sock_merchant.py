#!/bin/python3

# https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    
    sortedSocksHashMap = {}   
    for _ in ar:
        if _ in sortedSocksHashMap:
            sortedSocksHashMap[_] += 1
        else:
            sortedSocksHashMap[_] = 1

    pairs = 0
    for key in sortedSocksHashMap:
        pairs += int(sortedSocksHashMap[key] / 2)
        
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
