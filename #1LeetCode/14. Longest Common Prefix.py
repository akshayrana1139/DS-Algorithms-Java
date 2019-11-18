
from typing import List


# Runtime: 28 ms, faster than 98.18% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = "";i = 0
        min_len  = len(min(strs)) if len(strs)>0 else 0
        while(i<min_len):
            val_i = "" 
            for items in strs:
                if val_i =="":
                    val_i = items[i]   
                if val_i != items[i]:
                    return s
                val_i == items[i]
            s+=val_i; i+=1 
        return s

s = Solution()
a = s.longestCommonPrefix(["", "b"])
print(a)