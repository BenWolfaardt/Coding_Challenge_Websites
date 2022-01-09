#!/bin/python3

# https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    
    valleys, level = 0, 0

    for step in range(steps):
        if path[step] == 'U':
            level += 1
        else: # implies if path[step] == 'D':
            level -= 1
        
        if level == 0 and path[step] == 'U':
            valleys += 1
    return valleys

import unittest

class Test(unittest.TestCase):

    tests = [
        [12, "DDUUDDUDUUUD", 2],
        (8, "UDDDUDUU", 1)
    ]

    def testAllSeqence(self):
        for [steps, path, expected] in self.tests:
            actual = countingValleys(steps, path)
            assert actual == expected

if __name__ == "__main__":
    unittest.main()
