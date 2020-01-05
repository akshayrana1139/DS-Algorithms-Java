
# Runtime: 28 ms, faster than 92.65% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Reverse Linked List.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while(curr): 
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt
        return prev
        