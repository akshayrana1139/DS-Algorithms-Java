# Runtime: 44 ms, faster than 85.08% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        if head is None: return False
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next 
            if (fast):
                if slow.val == fast.val:
                    return True
        return False