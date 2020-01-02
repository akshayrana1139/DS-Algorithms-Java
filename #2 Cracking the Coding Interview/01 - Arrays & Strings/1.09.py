'''
String Rotation; Assume you have a method i s S u b s t r i n g which checks if one word is a 
substring of another. Given two strings, si and s2, write code to check if s2 is a rotation of s1 
using only one call to isSubstring (e.g.,"waterbottle"isa rotation of'erbottlewat").

Initial Thoughts: if a rotation, does it mean is should have all the letters in both string?

Didnt quite understand the question... Looked the answer to get more understanding. 

ANSWER from book:

In a rotation, we cut si into two parts, x and y, and rearrange them to get s2.
si = xy = waterbottle 
x = wat
y = erbottle
s2 = yx = erbottlewat

So, we need to check if there's a way to split si into x and y such that xy = si and yx = s2. Regardless of where the division between x and y is, 
we can see that yx will always be a substring of xyxy.That is, s 2 will always be a substring of s i s 1.

So the catch is that yx will always be a substring of xyxy.. 
so check if s2 is substring of s1+s1

def isrotaion(str1, str2):
    new_str = str1+str1
    return str2 in new_str

'''


def isrotaion(str1, str2):
    new_str = str1+str1
    return str2 in new_str


if __name__ == "__main__":
    print(isrotaion(str1="waterbottle", str2="erbottlewat"))