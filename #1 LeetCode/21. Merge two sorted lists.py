# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Runtime: 28 ms, faster than 95.06% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tail = head = ListNode(None)
        while(l1 and l2):
            if l1.val<=l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
            
        if l1: tail.next = l1
        if l2: tail.next = l2
        return head.next