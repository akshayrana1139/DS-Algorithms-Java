'''
Question: Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards, A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat""atco eta" etc.)

Initial Thoughts: This looks tough, because we cant directly check for palindrome because the word is a permutation.
Had it been a simple word, I would have scanned from the middle towards both end and compared each letter to confirm if it is a palindrome. 

From the example it seems we can ignore spaces, and they dont need to be in the order for palindrome. so we can focus only on the letters. 
Could ask question about casing? but seems like we can ignore that as well. 

#1 If we can sort the list and see but it wont help us find palindrome. We need to try to construct a palindrome out of the word. 
So how can we make a word paindrome.. keep the same letters in the first and last, oh which means every letter should appear twice except one letter if it has odd length. 

#2. I can may be create a hashmap of all the words and the every words with multiple value can be arranged in any fashion(since it doesnt need to be a dictionary word)
So basially we dont even need to arrange the words, we just need to check the count of each word.. 

So basic pseudocode is.. 

if the length is odd: 1 letter count can be 1 and the rest have to be present atleast 2times. 
if it is even, every letter should occure twice..

Lets try to find corner cases for the above pseudocode.. 

"akshay": its not coz k, s, h occurs only once.
"nana": both letters twice.. so can arrange nana, naan, anna, 
"appla" : 'aplpa', 'palap', so here letter l can occure once since it is odd.  

#1 first method could be to put in dict and then count each value.. This is O(n) + O(n)

def is_palindrome_permutation(str1):
    a = {}
    for char in str1:
        if char in a:
            a[char] += 1
        else:
            a[char] = 1
    
    count = 0
    str_len  = len(str)
    for key,value in a.items():
        if str_len%2 == 0:
            if value%2 != 0:
                return False
        else:
            if value == 1 or value%2 != 0: ## we can have a case where the extra value in odd is a repetetive term
                count +=1
    if count>1:
        return False
    else:
        return True
                
        


While writing code I realise it could be even number of times and not atleast 2..I realised another flaw as to how to find the bug in the dict. 
So i made the required changes as to what I was thinking and modified the code above,

'''

def is_palindrome_permutation(str1):
    a = {}
    len_count = 0
    str1 = str1.lower()
    for char in str1:
        if char != " ":
            len_count += 1
            if char in a:
                a[char] += 1
            else:
                a[char] = 1
    
    count = 0
    str_len  = len_count
    for _,value in a.items():
        if str_len%2 == 0:
            if value%2 != 0:
                return False
        else:
            if value == 1 or value%2 != 0: ## we can have a case where the extra value in odd is a repetetive term
                count +=1
    if count>1:
        return False
    else:
        return True


# While writing code from pseducode, I realised I forgot to took care of the spaces, I should ignore them before filling into the dict. 
# I also realised the length of string could have spaces in them, so I need to remove that and count it differently.
# I also forgot to lower case the letter before inserting them in dict.

if __name__ == "__main__":
    print(is_palindrome_permutation("akshay"))
    print(is_palindrome_permutation("apple"))
    print(is_palindrome_permutation("appla"))
    print(is_palindrome_permutation("nanana"))
    print(is_palindrome_permutation("naaan"))
    print(is_palindrome_permutation("nanan"))
    print(is_palindrome_permutation("Tact Coa"))


## After seeing the answer I realised we dont necessarily need to store the count, we could basically turn a flag on or off based on even times. 
## Or using bitwise operation, we could just turn the bit 0 or 1, and then we could be left with just one bit that was 1 which could be the palindrome then, we could handle it better but its ok to not know that. 

    
    