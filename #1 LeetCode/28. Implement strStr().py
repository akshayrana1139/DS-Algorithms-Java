# Runtime: 20 ms, faster than 98.10% of Python3 online submissions for Implement strStr().
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Implement strStr().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack): return -1
        if len(needle)==0: return 0
        
        l_s = len(haystack)
        l_n = len(needle)
        l = 0 
        r = l_n
        while(r<=l_s):
            if haystack[l:r]==needle:
                return l
            l+=1
            r+=1
        return -1
        