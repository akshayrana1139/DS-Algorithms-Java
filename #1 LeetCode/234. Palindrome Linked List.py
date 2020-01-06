# Definition for singly-linked list.


# Runtime: 56 ms, faster than 99.18% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 22.8 MB, less than 100.00% of Python3 online submissions for Palindrome Linked List.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# pushing everything into stack. 
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        a = []
        
        if slow is None:
            return True
        elif slow.next is None:
            return True
        
        while(slow):
            a.append(slow.val)
            slow = slow.next
    
        slow = head
        
        while(slow):
            if a.pop() != slow.val:
                return False
            slow = slow.next
        return True
            
            
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    Solution().isPalindrome(head)
        