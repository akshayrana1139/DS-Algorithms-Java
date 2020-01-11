# Runtime: 56 ms, faster than 97.72% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 13.6 MB, less than 69.11% of Python3 online submissions for Maximum Subarray.

# O(n) solution using Kadane Algorithm, https://en.wikipedia.org/wiki/Maximum_subarray_problem
# Explanation from: https://www.youtube.com/watch?v=86CQq3pKSUw

class Solution():
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if cur_sum < 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            
            if cur_sum > max_sum:
                max_sum = cur_sum
        
        return max_sum