'''
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2blc5a3. If the "compressed "string would not become smaller than the original string, your method should return the original string. 
You can assume the string has only uppercase and lowercase letters (a - z),

Intial thoughts: The casing is imp and have to be treated diffrntly.. could same letter only appear at same place or it can be fragmented? 
Example: 
aabbccaa -> a4b2c2? or is it a2b2c2a2

using another string/array.. as far as prev_value is same as current_value, keep counting, as new_value comes, add it in string and reset counter. 

def compress(str1):
    count = 0
    str2 = "" 
    for index, value in enumerate(str1):
        if index == 0:
            prev_value = value
            count += 1 
        elif prev_value == value:
            count += 1
        else:
            str2 += prev_value+str(count)
            count = 0
            prev_value = value
    if len(str2) == len(str1):
        return str1
    else:
        return str2
        

'''

def compress1(str1):
    count = 0
    str2 = "" 
    for index, value in enumerate(str1):
        if index == 0:
            prev_value = value
            count += 1 
        elif prev_value == value:
            count += 1
        else:
            str2 += prev_value+str(count)
            count = 1
            prev_value = value

    if len(str2) == len(str1):
        return str1
    else:
        return str2


def compress2(str1):
    count = 0
    str2 = "" 
    for index, value in enumerate(str1):
        if index == 0:
            prev_value = value
            count += 1 
            continue
        elif prev_value == value:
            count += 1
            continue
        else:
            str2 += prev_value+str(count)
            count = 1
            prev_value = value
    if index == len(str1)-1:
        str2 += prev_value+str(count)

    if len(str2) == len(str1):
        return str1
    else:
        return str2

if __name__ == "__main__":
    print(compress1("aabbbccdd"))   
    ## this printed a2b3c2.. I forgot that the last value d will never be printed coz it will never go in else block..
    ## So i had to make some changes.. 
    print(compress2("aabbbccdd"))   

## the official answer considers java where we should know the memory size in advance.. 
## so they make two loops, first sweep to count the length and second sweep to fill it in the correctly sized array/string builder
 