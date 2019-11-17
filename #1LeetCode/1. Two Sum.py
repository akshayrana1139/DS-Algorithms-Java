
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

from typing import List 

# Brute force way : Faster than 5%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Two passes: Faster than 98% 
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]]=i
        for i in range(len(nums)):
            if target-nums[i] in map:
                if map[target-nums[i]] != i:
                    return [i,map[target-nums[i]]]

# Runtime: 40 ms, faster than 99.79% of Python3 online submissions for Two Sum.
# Memory Usage: 14.1 MB, less than 63.49% of Python3 online submissions for Two Sum.
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if target-nums[i] in map:
                return [map[target-nums[i]],i]
            map[nums[i]]=i


s  = Solution3()
a = s.twoSum([3,3, 2, 4], 6)
print(a)
