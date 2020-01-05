
# Runtime: 12 ms, faster than 100.00% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:        
        behind = ahead = head
        count = 1
        while(count<=n):
            ahead = ahead.next 
            count += 1
        
        ## had to write this for passing the test case where n=1 for list with just one node. 
        if ahead is None:
            return head.next
        
        while(ahead.next is not None):
            behind = behind.next
            ahead = ahead.next
        
        behind.next = behind.next.next
        return head
        