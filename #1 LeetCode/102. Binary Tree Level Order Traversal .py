# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

#  Solution by: https://www.youtube.com/watch?v=1t7-G3ls7VI


# Runtime: 28 ms, faster than 91.28% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.
class Solution(object):
    def levelOrder(self, root):
        if root is None: return []
        que = deque()
        que.append(root)
        main_arr =[]
        while(len(que)>0):
            que_size = len(que)
            arr = []
            for i in range(que_size):
                node = que.popleft()
                arr.append(node.val)
                if node.left: 
                    que.append(node.left)
                if node.right: 
                    que.append(node.right)
            main_arr.append(arr)
        return main_arr
        
    
    