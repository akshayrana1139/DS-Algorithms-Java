import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # This is 2*O(n) runtime and O(n) memory

        # stack = []
        # for val in s:
        #     if val.lower() not in string.punctuation and val!=" ":
        #         stack.append(val.lower())

        # for val in s:
        #     if val not in string.punctuation and val!=" ":
        #         if stack.pop() != val.lower():
        #             return False
        # return True

# Runtime: 52 ms, faster than 42.88% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 13.4 MB, less than 72.62% of Python3 online submissions for Valid Palindrome.
        if len(s)==1: return True
        if len(s)==0: return True
        s = s.lower()
        l = 0
        r = len(s)-1
        while(l<r):
            if s[l] in string.punctuation or s[l]==" ":
                l+=1
                continue
            elif s[r] in string.punctuation or s[r]==" ":
                r-=1
                continue
            else:
                print(s[l], s[r])
                if s[l]!=s[r]:
                    
                    return False
            l+=1
            r-=1
        return True

if __name__ == "__main__":
    Solution().isPalindrome("A man, a plan, a canal: Panama")
        


                    