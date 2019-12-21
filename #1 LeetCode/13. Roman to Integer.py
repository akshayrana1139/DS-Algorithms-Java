

# Runtime: 44 ms, faster than 94.89% of Python3 online submissions for Roman to Integer.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = ((1000,'M'),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"), (3, "III"), (2, "II"), (1, "I"))
        num = 0
        for i,val in dic:
            while(val in s[0:len(val)]):
                index = s.index(val)
                s = s[index + len(val):]
                num=num+i
        return num

s = Solution()
print(s.romanToInt("XX"))