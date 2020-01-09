
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