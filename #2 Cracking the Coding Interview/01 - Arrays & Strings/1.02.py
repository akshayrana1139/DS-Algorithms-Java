
'''
Question: Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

Thoughts: Same casing?, obviously trim the string before processing? Example: god & dog

Initial Solutions: 

if different length, reject directly.. 
#1: check every character presence in the second string and reject if not found.. O(n^2) :(
#2: Above method though brute force still wont work because if you have multiple charachters like "godd" vs "dogg", its gonna approve it which is incorrect. 
#3: Since the count is important, I could think of hashtable with key being the char and the value being the count of it.. So we can make two such dict and compare them which is 2*Addition + 2*Scan dict. Works but bad.
#4: Need something better.. what if we sort both of them and then compare each indices and reject .. this is O(nlogn) for sorting + O(n) for comparing. 
#5: Can we do better? #3 looks more like a O(n) 

def is_permutation(str1, str2):
    dict1 = {}; dict2 = {}

    ## converting string to the dictionary/arrays(use ascii value for index) 
    for i in range(len(str1)):
        if str1[i] not in dict1:
            dict1[str1[i]] = 1
        else:
            dict1[str1[i]] += 1
        if str2[i] not in dict2:
            dict2[str2[i]] = 1
        else:
            dict2[str2[i]] += 1

    ## lookup values and compare both dict
    for key in dict1.items():
        if key in dict2:
            if dict1[key] != dict2[key]:
                return false
        else:
            return false
            
    return true

'''

## O(n) + O(n)
def is_permutation(str1, str2):
    dict1 = {}; dict2 = {}

    if len(str1) != len(str2):
        return False

    ## converting string to the dictionary/arrays(use ascii value for index) 
    for i in range(len(str1)):
        if str1[i] not in dict1:
            dict1[str1[i]] = 1
        else:
            dict1[str1[i]] += 1
        if str2[i] not in dict2:
            dict2[str2[i]] = 1
        else:
            dict2[str2[i]] += 1
            
    ## lookup values and compare both dict
    for key in dict1.keys():
        if key not in dict2:
            return False
        elif dict1[key] != dict2[key]:
            return False
    return True


if __name__ == "__main__":
    print(is_permutation("akshay", "rana"))
    print(is_permutation("god", "dog"))
    print(is_permutation("godd", "dogg"))

    