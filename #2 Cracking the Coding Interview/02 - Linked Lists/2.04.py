'''
Question: Partition; Write code to partition a linked list around a value x, such that all nodes less than x come before all
 nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than 
 x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the 
 left and right partitions.

EXAMPLE
input: 3 -> S -> 8 -> 5 -> 10 -> 2 -> 1
[partition=5] 
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

Thoughts: Since we dont need to sort it out, we just need to split data on the basis of partition.. 
we can create another list of values greater than the partition while we are traversing, we can remove the values as we go and keep adding in the new list.
In the end we can combine the two list.. 

while(curr.next != None):
    new_list = LinkedList()
    if curr.data>=partition:
        new_list.add(curr) ## add in new list
        prev.next = curr.next.next ## remove from curr list
    prev = curr
    curr = curr.next 

# as curr would be the last element in the list, so we can join these two lists.  
curr.next = new_list.head

'''