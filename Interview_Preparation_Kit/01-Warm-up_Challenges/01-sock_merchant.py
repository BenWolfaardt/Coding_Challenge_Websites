#!/bin/python3

# https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

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

import unittest

class Test(unittest.TestCase):

    tests = [
        [9, [10, 20, 20, 10, 10, 30, 50, 10, 20], 3],
        (10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3], 4)
    ]

    def testAllSeqence(self):
        for [n, ar, expected] in self.tests:
            actual = sockMerchant(n, ar)
            assert actual == expected

if __name__ == "__main__":
    unittest.main()
    