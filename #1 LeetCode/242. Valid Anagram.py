
# Runtime: 52 ms, faster than 39.26% of Python3 online submissions for Valid Anagram.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Valid Anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = collections.Counter(s)
        if len(s) != len(t): return False
        for val in t:
            if val not in dic:
                return False
            else:
                dic[val]-=1
                
        for key,value in dic.items():
            if value!=0:
                return False
        return True