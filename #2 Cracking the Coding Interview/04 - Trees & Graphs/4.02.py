'''
Question: Minimal Tree: Given a sorted (increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree with minima! height.

If we need minimum height, we need to put equal elements in both left and right side of the tree.. 
so we basically need the element at the centre of the sorted array. That way we get to make a balanced binary search tree.

Since the list is already sorted, we can find the middle number and split the list in two parts.. 
and then do this recursively.. 

def create_BST(int arr[], int start, int end):
    mid = (start+end)/2
    if(endt<start)## Need to think that. this took time though
        return Null

    TreeNode n = TreeNode(arr[mid])
    n.left = create_BST(arr, start, mid-1)
    n.right = create_BST(arr, mid+1, end)
    return n;
'''

class Tree():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():

    def __init__(self):
        pass

    @staticmethod
    def create_BST(abc):
        pass 


def create_s():
    pass

