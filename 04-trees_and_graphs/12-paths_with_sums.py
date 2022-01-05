#------------------------------------------------------Question------------------------------------------------------#

# ou are given a binary tree in which each node contains an integer value (which
# might be positive or negative). Design an algorithm to count the number of paths that sum to a
# given value. The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).

#--------------------------------------------------------Tips--------------------------------------------------------#

# 006 - Try simplifying the problem. What if the path had to start at the root?
# 014 - Don't forget that paths could overlap. For example, if you're looking for the sum 6, the
#       paths 1->3->2 and 1->3->2->4->-6->2 are both valid.
# 052 - If each path had to start at the root, we could traverse all possible paths starting from
#       the root. We can track the sum as we go, incrementing totalPaths each time we
#       find a path with our target sum. Now, how do we extend this to paths that can start
#       anywhere? Remember: Just get a brute-force algorithm done. You can optimize later.
# 068 - To extend this to paths that start anywhere, we can just repeat this process for all nodes.
# 077 - If you've designed the algorithm as described thus far, you'll have an O(N log N)
#       algorithm in a balanced tree. This is because there are N nodes, each of which is at depth
#       O(log N) at worst. A node is touched once for each node above it. Therefore, the N
#       nodes will be touched O(log N) time. There is an optimization that will give us an
#       O(N) algorithm.
# 087 - What work is duplicated in the current brute-force algorithm?
# 094 - Consider each path that starts from the root (there are N such paths) as an array. What
#       our brute-force algorithm is really doing is taking each array and finding all contiguous
#       subsequences that have a particular sum. We're doing this by computing all subarrays
#       and their sums. It might be useful to just focus on this little subproblem. Given an array,
#       how would you find all contiguous subsequences with a particular sum? Again, think
#       about the duplicated work in the brute-force algorithm.
# 103 - We are looking for subarrays with sum targetSum. Observe that we can track in
#       constant time the value of runningSum i , where this is the sum from element O through
#       element i. For a subarray of element i through element j to have sum targetSum,
#       runningSum(subscript i - 1) + targetSum must equal runningSum(subscript j) (try drawing a picture of
#       an array or a number line). Given that we can track the runningSum as we go, how can
#       we quickly look up the number of indices i where the previous equation is true?
# 108 - Try using a hash table that maps from a runningSum value to he number of elements
#       with this runningSum.
# 115 - Once you've solidified the algorithm to find all contiguous subarrays in an array with a
#       given sum, try to apply this to a tree. Remember that as you're traversing and modifying
#       the hash table, you may need to "reverse the damage" to the hash table as you traverse
#       back up.

#------------------------------------------------------Solution------------------------------------------------------#

# my own implementation, no idea what the O() is for this solution and did not use the above hints..

class Node():
  def __init__(self, key=None):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None

#--------------------------------------------------------Tree--------------------------------------------------------#

# n1 = Node(7)
# n2 = Node(4)
# n3 = Node(9)
# n4 = Node(5)
# n5 = Node(-2)
# n1.left = n2
# n1.right = n3
# n2.left = n4
# n2.right = n5
# n2.parent = n1
# n3.parent = n1
# n4.parent = n2
# n5.parent = n2

from BinaryTree import BinaryTree 

t1 = BinaryTree()
n1 = t1.insert(10, None)
n2 = t1.insert(5, n1)
n3 = t1.insert(-3, n1)
n4 = t1.insert(3, n2)
n5 = t1.insert(2, n2)
n6 = t1.insert(3, n4)
n7 = t1.insert(-2, n4)
n8 = t1.insert(1, n5)
n9 = t1.insert(11, n3)
n10 = t1.insert(8, n9)
n11 = t1.insert(-8, n10)

#--------------------------------------------------------------------------------------------------------------------#

global i, counter, sum
index, counter, value = 0, 0, 8
sum = n1.key
traversal = []
traversal.append(n1.key)

# parse root nood initially
def traverse(node):
    if node.key == None:
        return
   
    global index, counter, sum

    while traversal != None:
        if sum == value:
            counter += 1
        if node.left != None:
            index += 1
            traversal.append(node.left.key)
            sum += traversal[index]
            traverse(node.left)
        if node.right != None:
            index += 1
            traversal.append(node.right.key)
            sum += traversal[index]
            traverse(node.right)
        if (node.left == None and node.right == None):
            counter = rootToLeafCheck(traversal, value)
            sum -= traversal[index]
            traversal.pop(index)
            index -= 1
            if index == -1:
                break
            if node.parent.left == None: 
                node.parent.right = None
            elif node.parent.left.key == node.key:
                node.parent.left = None
            break
    return counter       


def rootToLeafCheck(fullTraversal, value):
    global counter
    for i in range(1, len(fullTraversal)):
        sum = 0
        for j in range(i, len(fullTraversal)):
            sum += fullTraversal[j]
            if sum == value:
                counter += 1
    return counter

#-----------------------------------------------------Optimised-----------------------------------------------------#

def countPathsWithSum(node, targetSum, runningSum=0, pathCountHashTable=None):
    if pathCountHashTable == None:
        pathCountHashTable = {}
    if node == None:
        return 0
    runningSum += node.key
    totalPaths = pathCountHashTable.get((runningSum - targetSum), 0)

    # if runningSum equals targetSum, then one additional path starts at root. Add in this path
    if runningSum == targetSum:
        totalPaths += 1

    # Increment pathCount, recurse, then deccrement pathCpunt
    incrementHashTable(pathCountHashTable, runningSum, 1) # increment pathCountHashTable
    totalPaths += countPathsWithSum(node.left, targetSum, runningSum, pathCountHashTable)
    totalPaths += countPathsWithSum(node.right, targetSum, runningSum, pathCountHashTable)
    incrementHashTable(pathCountHashTable, runningSum, -1) # decrement pathCount

    return totalPaths


def incrementHashTable(hashTable, key, delta):
    newCount = hashTable.get(key, 0) + delta
    if newCount == 0:
        hashTable.pop(key)
    else: 
        hashTable[key] = newCount

#--------------------------------------------------------Tests-------------------------------------------------------#

import unittest

class Test(unittest.TestCase):
  
    def testAllSequences(self):

        # self.assertEqual(traverse(n1), 3)
        self.assertEqual(traverse(n1), 5)

if __name__ == "__main__":
    # print(countPathsWithSum(n1, 9))
    print(countPathsWithSum(n1, 8))
    unittest.main() # actual tests (Ben method)
    # check if the assert statement's value is equal to that of the optimised method.

    # TODO: fix Ben's method, I need to implement the other for loop that I originally had because I'm counting the same things mutliple times.
    # have an index = 0 flag to allow the rootToLeafCheck to be run twice, for its main left and right nodes, and then use the other function for all calls
    