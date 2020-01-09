# Runtime: 24 ms, faster than 97.27% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if (t1 is None and t2 is None):
                return True
            if (t1 is None or t2 is None):
                return False
            return (t1.val == t2.val) and isMirror(t1.right, t2.left) and  isMirror(t1.left, t2.right)
        return isMirror(root, root)