# Runtime: 212 ms, faster than 70.45% of Python3 online submissions for Reverse String.
# Memory Usage: 17 MB, less than 100.00% of Python3 online submissions for Reverse String.

from typing import List

# two pointers and swap
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0; r = len(s) - 1
        while(l<r):
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l+=1; r-=1
        