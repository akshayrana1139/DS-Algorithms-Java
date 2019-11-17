# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

# Note:

# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# Example 1:

# Input: "42"
# Output: 42


class Solution:
    def check_limit_and_return(self, l, isNeg):
        l = -l if isNeg else l
        if l<-2**31:
            return -2**31
        elif l>(2**31)-1:
            return (2**31)-1
        else:
            return l 
    
    
    def myAtoi(self, str: str) -> int:
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        sign = ["+","-"]
        spaces = ["", " "]
        l = 0; isNeg = False; prev_value = ''; isStarted = False
        for char in str:
            if isStarted:
                if char not in numbers:
                    return  self.check_limit_and_return(l, isNeg) # anything other than num, return number
                else:
                    l = l*10 + int(char)
            else:
                if char not in numbers + sign + spaces: # if word return 0
                    return 0
                elif char in spaces: # if spaces, continue
                    continue
                elif char in numbers: # if number, start counting
                    isStarted = True
                    l = l*10 + int(char)
                elif char in sign and prev_value not in sign: # if sign, keep a note, 
                    isStarted = True
                    isNeg = True if char == "-" else False
                elif char in sign and prev_value in sign: # if sign and prev_value is sign, return number
                    return self.check_limit_and_return(l, isNeg)
        return self.check_limit_and_return(l, isNeg)


        

s = Solution()
print(s.myAtoi("5-6"))