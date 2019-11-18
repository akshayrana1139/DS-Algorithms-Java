


# Runtime: 40 ms, faster than 98.21% of Python3 online submissions for Integer to Roman.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Integer to Roman.
class Solution:
    def intToRoman(self, num: int) -> str:
        dic = ((1000,'M'),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"), (3, "III"), (2, "II"), (1, "I"))
        s = ""
        for i,val in dic:
            while(num>=i):
                s+=val
                num-=i
        return s

s = Solution()
print(s.intToRoman(20))