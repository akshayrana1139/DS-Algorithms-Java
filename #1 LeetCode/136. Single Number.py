# Runtime: 76 ms, faster than 99.25% of Python3 online submissions for Single Number.
# Memory Usage: 15.3 MB, less than 8.20% of Python3 online submissions for Single Number.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = collections.Counter(nums)
        
        for key,value in dic.items():
            if value==1:
                return key
            
        