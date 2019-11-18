from typing import List


## timeout : 2 pass
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i,iv in enumerate(height):
            j = i + 1
            while(j<len(height)):
                vj = height[j]
                area = min(iv,vj)*(abs(j-i))
                max_area = max(area, max_area)
                j = j + 1
        return max_area

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))

# 1 pass
# Runtime: 136 ms, faster than 88.75% of Python3 online submissions for Container With Most Water.
# Memory Usage: 14.6 MB, less than 8.42% of Python3 online submissions for Container With Most Water.
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i=0; j = len(height) - 1
        while(i<j):
            iv = height[i]
            vj = height[j]
            area =  min(iv,vj)*(abs(j-i))
            max_area = max(max_area, area)
            if iv<vj:
                i+=1
            else:
                j-=1
        return max_area