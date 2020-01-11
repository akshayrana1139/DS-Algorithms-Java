
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Runtime: 160 ms, faster than 86.66% of Python3 online submissions for Intersection of Two Linked Lists.
# Memory Usage: 28 MB, less than 100.00% of Python3 online submissions for Intersection of Two Linked Lists.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptr1 = headA
        ptr2 = headB
        counta = countb = 0
        while(ptr1 or ptr2):
            if ptr1:
                counta+=1
                ptr1 = ptr1.next
            if ptr2:
                countb+=1
                ptr2 = ptr2.next
        # Ran till the end and found the count of both lists


        # Setting up the ptrs in the same spot, specifically jumping for the
        # longer one  
        if counta<countb:
            count = 0
            diff = countb-counta
            while(count<diff):
                count+=1
                headB = headB.next
        elif countb<counta:
            count = 0
            diff = counta-countb
            while(count<diff):
                count+=1
                headA = headA.next
                
        while(headA):
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None