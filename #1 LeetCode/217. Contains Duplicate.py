# Runtime: 120 ms, faster than 93.65% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 18 MB, less than 88.68% of Python3 online submissions for Contains Duplicate.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = set()
        for i in nums:
            if i in dic:
                return True
            else:
                dic.add(i)
        return False