

'''

My different methods I tried in google doc initially.. 

    ## Sort and check  
    def if_unique(str): 
        str.sort() 
        for index in range(len(str)-1):
        if var[index] == var[index+1]:
            return false
        return true

    ## Using array
    def if_unique(str): 
        a = [] 
        for char in str:
        if a[convert_int(char)]:
            return true
            a[convert_int(char)] = true 
        return false

    ## Using hashset
    def if_unique(str): 
        a = set()
        for char in str:
        if char in a:
            return true
            a.add(char)  
        return false
'''

def if_unique(input_string):
    a = set()
    for char in input_string:
        if char in a:
            return True
        a.add(char)  
    return False

if __name__ == "__main__":
    print(if_unique("akshay"))
    print(if_unique("singh"))