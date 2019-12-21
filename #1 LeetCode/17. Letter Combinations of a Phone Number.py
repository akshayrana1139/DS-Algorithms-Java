
# Runtime: 20 ms, faster than 99.75% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Letter Combinations of a Phone Number.
from typing import List
class Solution:
    dic = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
    }
    
    def combine(self,a, digit):
        new_a = []
        for i in a:
            print(self.dic[digit])
            for letter in self.dic[digit]:
                new_a.append(i+letter)
        return new_a 
    
    def letterCombinations(self, digits: str) -> List[str]:
        
        a = ['']
        for i in digits:
            a = self.combine(a, i)
        return a if len(a)>1 else []

s = Solution()
print(s.letterCombinations("23"))
            