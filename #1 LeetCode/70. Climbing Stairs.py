
# Runtime: 24 ms, faster than 83.39% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.

# A better fibonnaci formula exists to do it in logn times. but not required for now. 
class Solution:
    def climbStairs(self, n: int) -> int:
        if (n==1): return 1
        if (n==2): return 2
        i=3; first = 1; second = 2
        while(i<=n):
            final = first+second
            first = second
            second = finl
            i+=1
        return final