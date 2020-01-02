'''
Question: Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. 
The digits are stored in reverse order, such that the 1's digit is at the head of the iist. 
Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
input;(7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295. Output; 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. 
Input(6 -> 1 -> 7) + (2 -> 9 -> S).That is,617 + 295. Output: 9 -> 1 -> 2.That is, 912.


Thoughts: I feel the follow up is much easier where you could just sum up the heads and store the carry and go on with the next values. I might be missing a catch

I think the other way is to convert the list to a number and which makes the reverse part much easier. 
for ex: 7>1>6, pick the first value.. and store it as 7,
second value comes but multiplies with 10 and add to previous value so it becomes 10+7 = 17
third value come and multiplies with 100 and add to previous.. 600+17 = 617.

We can do the same process for another list and get the number.. Now we need to convert the number back to the list.. 
for ex 617 to be converted back to 7->1->6

617%10 =I will get 7 and put it as a head of a list..
617/10 = 61
so now 61%10 = 1 where I can put 7.next = 1, then just repeat the task..

PSEUDOCODE:

def sum_nodes_list(list1, list2):
    curr = list1.head
    val1 = 0 
    count = 0
    while(curr.next != None):
        val = curr.data
        val1 += val*(10**count)

    # repeat the same for list2 
    # sum  = val1 + val2
    # convert val2 back to list
    new_list = Linkedlist()
    while(sum>0):
        num = sum%10
        new_node.next = num ## this part of adding removing nodes depends if u implement it as a stack or a queue
        num = int(num/10)
    return new_node


ANOTHER APPROACH IS DIRECT WHERE WE DIRECTLY ADD VALUES OF NODES alongwith carries. SOUND EASY THOUGH.


'''