# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}; count = 0; max_count = 0; ptr = 0
        for index,char in enumerate(s):
            if char in map and map[char] >= ptr:
                max_count = max(max_count,count)
                count = index - map[char]
                ptr = map[char] + 1
            else:
                count+= 1
            map[char] = index
        return max(count,max_count)


s = Solution()
print(s.lengthOfLongestSubstring("abcba"))
