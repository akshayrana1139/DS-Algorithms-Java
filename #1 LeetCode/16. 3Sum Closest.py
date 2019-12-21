# Given an array nums of n integers and an integer target, find three integers in nums such that the sum 
# is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.


# Runtime: 112 ms, faster than 88.52% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for 3Sum Closest.
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        min_df = 10000
        for i,v in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            need = target - v
            while(l<r):
                sums = nums[l] + nums[r]
                if abs(need-sums)<min_df:
                    min_df = abs(need-sums)
                    ans = sums+v 
                if min_df == 0:
                    return ans
                if sums<=need:
                    l+=1
                else:
                    r-=1
        return ans



s = Solution()
print(s.threeSumClosest([0,1,2], 3))