'''
Question: Validate BST: Implement a function to check if a binary tree is a binary search tree.

I thought of in-traversal to add elements in a array.. and then to compare if the array is sorted.. 
Or even better aproach is to compare value in a tree itself and return false as soon as it doesnt follow left<root<right.

But my method fails because we can have a tree like this.. 

      7
    3     8
  1   9  6  9

  Here both 9 after 3 and 6 after 8 is incorrect but my algorithm above will pass it.. 

So the final solution is to keep a track of lower and upper bounds as well while traversing.

'''


#Approach 1: To get everything in the array using in-traversal 

# Definition for a binary tree node.

# Runtime: 40 ms, faster than 84.77% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 15.5 MB, less than 100.00% of Python3 online submissions for Validate Binary Search Tree.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        arr = []
        
        def add_in_array(root: TreeNode, arr: List):
            if root is None:
                return 0
            add_in_array(root.left, arr)
            arr.append(root.val)
            add_in_array(root.right, arr)
          
        add_in_array(root, arr)
        
        for i in range(len(arr)-1):
            if arr[i]>=arr[i+1]:
                return False
        return True


## We can even use stacks with iteration algorithm..

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
            
        stack = [(root, float('-inf'), float('inf')), ] 
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True 