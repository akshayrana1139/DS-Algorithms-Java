# 7. Reverse Integer

# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21



# Runtime: 24 ms, faster than 99.19% of Python3 online submissions for Reverse Integer.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Reverse Integer.
class Solution:
    def reverse(self, x: int) -> int:
        # return 0 when reversed integer overflows and not original number
        li = 0; sign = False if x<0 else True
        while x!=0:
            # print(li)
            li = li*10 + abs(x)%10
            x = int(x/10)
         # Incorrect way as li shouldnt be able to store more than the range
        if li>-2**31 and li<(2**31)-1:
            return li if sign else -li
        else:
            return 0

s = Solution()
print(s.reverse(-123))