
# Runtime: 84 ms, faster than 89.53% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for First Unique Character in a String.
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int: 
        # dic = {}
        # for i in s:
        #     if i in dic:
        #         dic[i]+=1
        #     else:
        #         dic[i]=1
                
        dic = collections.Counter(s)
                
        for index in range(len(s)):
            if dic[s[index]] == 1:
                return index
        return -1