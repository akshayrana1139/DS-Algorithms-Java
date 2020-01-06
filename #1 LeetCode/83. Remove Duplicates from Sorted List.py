
# Runtime: 36 ms, faster than 85.15% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while(p and p.next):
            if(p.val == p.next.val):
                p.next = p.next.next
            else:
                p = p.next
        return head