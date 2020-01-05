
# Runtime: 20 ms, faster than 97.73% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        opening = ['(', "{", "["]
        closing = [")", "}", "]"]
        a = []
        for i in s:
            if i in opening:
                a.append(i)
            elif i in closing:
                if len(a)==0:
                    return False
                else:
                    if dic[i] == a.pop():
                        continue
                    else:
                        return False
                
                
        if len(a)==0:
            return True
        else:
            return False     

       