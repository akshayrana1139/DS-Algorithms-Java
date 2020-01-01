'''
Question: URLify: Write a method to replace all spaces in a string with'%20'You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string, (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)

Initial thoughts: You can use trim to remove extra spaces, then left with only spaces between the words.. and use replace keyword :D 
Seriously: Do we actually need to move the preceding characters by three indices when we insert %,2,0? And how do we deal with multiple spaces?

Do we need to make manipulations in the same string/array? Or can we make another one? 

If we can make another array.. keep inserting the same value when we find something other than space, and insert %20 if we find space.
But since we have the array true length, we might want to edit in the same string, and can start from reverse since the extra buffer is in the end. 

Example: "akshay rana"
True length: 11
Actual length with space: 13 
index = 13, index--
i = 11, i--
Start reverse order

We need two pointers, one for putting values, and one for actually moving letters
i = 11, index = 13: r
i = 10, index = 12: a
i = 09, index = 11: n
i = 08, index = 10: a
i = 07, index = 09: '' so put 0
        index = 08: put 2
        index = 07: put %
i = 06: index = 06: y
i = 05: index = 05: a
i = 04: index = 04: h

## Pseudocode

i = true_length - 1 ## assuming it true_length
index = actual_length + space - 1 ## assuming it actual_length

while(i>0):
    if str[i] == ' ':
        str[index-1] = "0"
        str[index-2] = "2"
        str[index-3] = "%"
        index = index - 3        
    else:
        str[index] = str[i]
        index -= 1

'''

def urlify(str1, true_length, actual_length):
    i = true_length - 1
    index = actual_length - 1
    while(i>=0):
        if str1[i] == ' ':
            str1[index-1] = "0"
            str1[index-2] = "2"
            str1[index-3] = "%"
            index -= 3
        else:
            str1[index] = str1[i]
            index -= 1
        i -= 1
    return str

if __name__ == "__main__":
    print(urlify("akshay rana  ", 11, 13))


