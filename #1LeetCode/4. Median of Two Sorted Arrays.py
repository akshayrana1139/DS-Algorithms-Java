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

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        length = len(nums3)
        if length%2 == 0 :
            a = int(length/2) - 1
            b = int(length/2)
            print(a,b)
            return (nums3[a] + nums3[b])/2
        else:
            a = int((length + 1)/2)
            return nums3[a]


s = Solution()
print(s.findMedianSortedArrays([1,2,3],[4,5,6]))
