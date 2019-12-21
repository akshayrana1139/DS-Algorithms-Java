# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true

# Runtime: 56 ms, faster than 95.08% of Python3 online submissions for Palindrome Number.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        else:
            if str(x) == str(x)[::-1]:
                return True
            else:
                return False

# s = Solution()
# print(s.isPalindrome(121))


## without converting to string
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        l = 0 
        actual_x = x
        if x < 0: 
            return False
        else:
            while x>=1:
                l = l*10 + x%10
                x = int(x/10)
        print(l)
        return True if l==actual_x else False
            
            
s = Solution2()
print(s.isPalindrome(121))