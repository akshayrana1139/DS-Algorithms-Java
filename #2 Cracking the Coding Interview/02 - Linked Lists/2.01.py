'''
Question: Remove Dups: Write code to remove duplicates from an unsorted linked list. 
FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed? Hints: #9, #40

Initial Thoughts: 
Thinking of a bad brute force way: have two pointers, one pointer stays at one node while the other compares it with every node.. O(n^2)
A better brute force way is to sort the list and then compare adjacent values.. a lil better but it is O(nlogn) + O(n)

Buffer: Using a dictionary to insert values as we proceed, and then raise a flag as soon as we encounter a duplicate, then remove that element. 
## current to be removed..
previous.next = current.next.next # if only single linked list..
This idea with buffer will take O(n) time and O(n) space..

Without buffer?: I guess we are only left with the runner method which is O(n^2)

'''