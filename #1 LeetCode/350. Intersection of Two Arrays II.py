from typing import List
class Solution:

    ## perfect if the order is important as well
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = 0
        r = 0
        final = []
        if len(nums1)<len(nums2):
            small = nums1
            large = nums2
        else:
            small = nums2
            large = nums1
        while(l<len(small) and r<len(large)):
            if small[l]==large[r]:
                final.append(small[l])
                r+=1
                l+=1
            else:
                r+=1
        return final
            
    # Runtime: 40 ms, faster than 94.02% of Python3 online submissions for Intersection of Two Arrays II.
    # Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays II.
    
    # If order is not important, could use hashmap.
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = collections.Counter(nums1)
        final = []
        for val in nums2:
            if val in dic1 and dic1[val]>0:
                final.append(val)
                dic1[val] -= 1
        return final
            