'''
Question: 2.6 Palindrome: Implement a function to check if a linked list is a palindrome,

Thoughts: 

#1: We could repeat our solution for the array, count the number of times the values appear, it should appear even times and only one value could appear odd time or 1 time if the length is odd.

In case no other data to be stored, we can use runer technique.. 

#2: We can reverse the linked list till we have reached half way.. (how to know if we reached half way? use second pointer with double jumps an if p2 reaches the end, p1 reaches the half)
how to reverse? Put them in a stack and then keep popping out the values and compare with values p1.next ( continue with p1)

'''