from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """  
        size = len(nums)
        n = 0
        
        while n < size:
            if nums[n] is 0:
                nums.pop(n)
                nums.append(0)
                size -= 1
            else:
                n += 1

if __name__ == "__main__":
    Solution().moveZeroes([0,1,0,3,12])