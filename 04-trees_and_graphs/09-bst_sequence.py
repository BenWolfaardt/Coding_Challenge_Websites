#------------------------------------------------------Question------------------------------------------------------#

# A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.

# Example: 

# Input:
#                  2
#                 / \
#                1   3

# Output: {2, 1, 3}, {2, 3, 1}

#--------------------------------------------------------Tips--------------------------------------------------------#

# 039 - What is the very first value that must be in each array?
# 048 - The root is the very first value that must be in every array. What can you say about the
#       order of the values in the left subtree as compared to the values in the right subtree? Do
#       the left subtree values need to be inserted before the right subtree?
# 066 - The relationship between the left subtree values and the right subtree values is, essen­
#       tially, anything. The left subtree values could be inserted before the right subtree, or the
#       reverse (right values before left), or any other ordering.
# 082 - Break this down into subproblems. Use recursion. If you had all possible sequences for
#       the left subtree and the right subtree, how could you create all possible sequences for
#       the entire tree?

#------------------------------------------------------Solution------------------------------------------------------#

def allSequences(node):
    result = []
    if node == None:
        return [[]]
    # recurse on left and right subtrees
    leftSeq = allSequences(node.left)
    rightSeq = allSequences(node.right)
    # weave together each list from the left and right sides
    for left in leftSeq:
        for right in rightSeq:
            result = weaveLists(left, right, [node.key], result) # key = value = data - different terminology
    return result

# weave lists together in all possible wasys. This algorithm works by removing the 
# head from one list, recursing, and then doing the same thing with th other list
def weaveLists(first, second, prefix, results):
    # one list is empt. Add remainder to [a copied] prefix and store result
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return results

    # recurse with head of first added to the prefix. 
    headFirst = first[0] 
    prefix.append(headFirst) # want it at the end
    results = weaveLists(first[1:], second, prefix, results)
    prefix.pop()
    # Do the same thing with second, damaging and then restoring the list
    headSecond = second[0] 
    prefix.append(headSecond) # want it at the end
    results = weaveLists(first, second[1:], prefix, results)
    prefix.pop()
    return results

#------------------------------------------------------Solution------------------------------------------------------#

# Another method

# Works, but the order of the output is slightly different hence the test failing, even though it lists all options

# def allSequences(bst):
#   return partialBSTSequences([], [bst])
  
# def partialBSTSequences(partial, subtrees):
#     if not len(subtrees):
#         return [partial]
#     sequences = []
#     for index, subtree in enumerate(subtrees):
#         nextPartial = partial + [subtree.key]
#         nextSubtrees = subtrees[:index] + subtrees[index+1:]
#         if subtree.right:
#             nextSubtrees.append(subtree.right)
#         if subtree.left:
#             nextSubtrees.append(subtree.left)
#         sequences += partialBSTSequences(nextPartial, nextSubtrees)
#     return sequences

#-------------------------------------------------------Example------------------------------------------------------#

# The below example makes use of parsing the BinarySearchTree Data Structure 

from BinarySearchTree import BinarySearchTree # used for example

def findBSTSequences(bst):
    if not bst.root:
        return []
    return allSequences(bst.root)

# the below numbers are the ones that they use in the book for the solution

def example():
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(15)
    bst.insert(10)
    bst.insert(25)
    bst.insert(20)
    bst.insert(50)
    bst.insert(60)
    bst.insert(70)
    bst.insert(65)
    bst.insert(80)

    sequences = findBSTSequences(bst)
    print(sequences)

#--------------------------------------------------------Tests-------------------------------------------------------#

import unittest

class Node():
  def __init__(self, key=None, left=None, right=None):
    self.key, self.left, self.right = key, left, right


class Test(unittest.TestCase):
  
  def testAllSequences(self):
    # note that it's finicky with regards to the order of the below, but the answer is still correct
    self.assertEqual(allSequences(Node(7,Node(4,Node(5)),Node(9))), [
        [7, 4, 5, 9],
        [7, 4, 9, 5],
        [7, 9, 4, 5]
    ])
    print(allSequences(Node(7,Node(4,Node(5)),Node(9))))

    # note that it's finicky with regards to the order of the below, but the answer is still correct
    self.assertEqual(allSequences(Node(7,Node(4,Node(5),Node(6)),Node(9))), [
        [7, 4, 5, 6, 9],
        [7, 4, 5, 9, 6],
        [7, 4, 9, 5, 6],
        [7, 9, 4, 5, 6],
        [7, 4, 6, 5, 9],
        [7, 4, 6, 9, 5],
        [7, 4, 9, 6, 5],
        [7, 9, 4, 6, 5]
    ])
    print(allSequences(Node(7,Node(4,Node(5),Node(6)),Node(9))))

if __name__ == "__main__":
  example() # example print out
  unittest.main() # actual tests
