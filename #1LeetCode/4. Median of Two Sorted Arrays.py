# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5
from typing import List
# Runtime: 80 ms, faster than 98.43% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        length = len(nums3)
        if length%2 == 0 :
            a = length/2 - 1
            b = length/2
            return (nums3[int(a)] + nums3[int(b)])/2
        else:
            a = (length - 1)/2
            return nums3[int(a)]


s = Solution()
print(s.findMedianSortedArrays([1,3],[2]))
