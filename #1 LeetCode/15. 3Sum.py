from typing import List

## duplicate triplets
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        a = []
        for index, target in enumerate(nums):
            i = index + 1
            while(i<len(nums)):
                find = -(target+nums[i])
                if find in dic:
                    if (dic[find] != index and dic[find] != i):
                        triplet = [target, nums[i], find]
                        a.append(triplet) 
                else:
                    dic[nums[i]] = i
                i += 1
        return a



## fixed duplicate triplets but it came O(n^2) + O(len(a)): Timeout, doesnt work :( ??
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        a = []
        for index, target in enumerate(nums):
            i = index + 1
            while(i<len(nums)):
                find = -(target+nums[i])
                if find in dic:
                    if (dic[find] != index and dic[find] != i):
                        triplet = [target, nums[i], find]
                        triplet.sort()
                        if triplet not in a:
                            a.append(triplet) 
                else:
                    dic[nums[i]] = i
                i += 1
        return a


## fixed duplicate triplets by sliding approach but after sorting numbers. This is O(nlogn) + O(n^2) + duplicate(O(n^3))

# Runtime: 660 ms, faster than 94.84% of Python3 online submissions for 3Sum.
# Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for 3Sum.
class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = []
        nums.sort()
        for i, target in enumerate(nums):
            if nums[i]>0:   break
            if i>0 and nums[i] == nums[i-1]:    continue
            l = i + 1
            r = len(nums) - 1
            while(l<r):
                sums = target + nums[l] + nums[r]
                if sums<0:
                    l+=1
                elif sums>0:
                    r-=1
                else:
                    a.append([target, nums[l], nums[r]])
                    ## duplicate check
                    while(l<r and nums[l] == nums[l+1]):
                        l+=1
                    while(l<r and nums[r] == nums[r-1]):
                        r-=1 
                    l += 1
                    r -= 1
        return a

s = Solution3()
print(s.threeSum([-1, 0, 1, 2,-1, -4]))