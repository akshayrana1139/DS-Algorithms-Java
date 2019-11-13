# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

## Brute force : Faster than 21% -- This is O(n^3), can go O(n^2) with DP and O(n) with Manacher's Algorithm
class Solution:
    def longestPalindrome(self, s: str) -> str:
        reverse_s = s[::-1]; r=''
        for j in reversed(range(len(s)+1)):
            for i in range(len(s)+1):
                if i+j<=len(s):
                    if s[i:i+j] == s[i:i+j][::-1]:
                        return s[i:i+j]
                else:
                    break
        return r

s = Solution()
print(s.longestPalindrome('aacdefcaa'))