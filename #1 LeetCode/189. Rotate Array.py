class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

# Timeout Error 

        ## Using O(kn), O(1) Memory
        
        # k = k%len(nums)
        # while(k>0):
        #     prev = nums[-1]
        #     for i in range(len(nums)):
        #         buffer = nums[i]
        #         nums[i] = prev
        #         prev = buffer
        #     k-=1
            
# Runtime: 52 ms, faster than 98.36% of Python3 online submissions for Rotate Array.
# Memory Usage: 14.1 MB, less than 5.09% of Python3 online submissions for Rotate Array.

        ## Using O(n) time and O(n) Memory
        # n = len(nums)
        # l = [None] * n
        # for i in range(n):
        #     total = (i+k)%n
        #     l[total] = nums[i]
        
        # for i in range(n):
        #     nums[i] = l[i]
        
1 

        