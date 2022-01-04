#------------------------------------------------------Question------------------------------------------------------#

# Given a sorted (increasing order) array with unique integer elements, write an algo­
# rithm to create a binary search tree with minimal height.

#--------------------------------------------------------Tips--------------------------------------------------------#

# 019 - A minimal binary tree has about the same number of nodes on the left of each node as
#       on the right. Let's focus on just the root for now. How would you ensure that about the
#       same number of nodes are on the left of the root as on the right?
# 073 - You could implement this by finding the "ideal" next element to add and repeatedly
#       calling insertValue. This will be a bit inefficient, as you would have to repeatedly
#       traverse the tree. Try recursion instead. Can you divide this problem into subproblems?
# 116 - Imagine we had a createMinimal Tree method that returns a minimal tree for a
#       given array (but for some strange reason doesn't operate on the root of the tree). Could
#       you use this to operate on the root of the tree? Could you write the base case for the
#       function? Great! Then that's basically the entire function.

#------------------------------------------------------Solution------------------------------------------------------#

# To create a tree of minimal height, we need to match the number of nodes in the left subtree to the number
# of nodes in the right subtree as much as possible. This means that we want the root to be the middle of the
# array, since this would mean that half the elements would be less than the root and half would be greater
# than it.

# We proceed with constructing our tree in a similar fashion. The middle of each subsection of the array
# becomes the root of the node. The left half of the array will become our left subtree, and the right half of
# the array will become the right subtree.

# One way to implement this is to use a simple root. insertNode(int v) method which inserts the
# value v through a recursive process that starts with the root node. This will indeed construct a tree with
# minimal height but it will not do so very efficiently. Each insertion will require traversing the tree, giving a
# total cost ofO ( N log N) to the tree.

# Alternatively, we can cut out the extra traversals by recursively using the createMinimalBST method.
# This method is passed just a subsection of the array and returns the root of a minimal tree for that array.

# The algorithm is as follows:

# 1. Insert into the tree the middle element of the array.
# 2. Insert (into the left subtree) the left subarray elements.
# 3. Insert (into the right subtree) the right subarray elements.
# 4. Recurse.

def createMinimalBST(sortedArray):
    if len(sortedArray) == 0:
        return None
    mid = (int) (len(sortedArray) / 2)
    left = createMinimalBST(sortedArray[:mid])
    right = createMinimalBST(sortedArray[(mid + 1):])
    return TreeNode(sortedArray[mid], left, right)

class TreeNode():

    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
    
    def __str__(self):
        string = "(" + str(self.data)
        if self.left:  string += str(self.left)
        else:          string += "."
        if self.right: string += str(self.right)
        else:          string += "."
        return string + ")"

# Although this code does not seem especially complex, it can be very easy to make little off-by-one errors.
# Be sure to test these parts of the code very thoroughly.

#--------------------------------------------------------Tests-------------------------------------------------------#

import unittest

class Test(unittest.TestCase):

    sortedArrays = (
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    )

    def test(self):
        
        for array in self.sortedArrays:
            bst = createMinimalBST(array)
            self.assertEqual(str(bst), "(5(3(2(1..).)(4..))(8(7(6..).)(9..)))")

if __name__== "__main__":
    unittest.main()
