'''
Question: Implement an algorithm to delete a node in the middle 
(i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

# Approach One
#1: since it is a singly linked list, we do need to iterate to that node and maintain a previous node while we are at it. 

once the current_node == actual_node..
previous.next = current.next ## thats all we need to remove it from the list. 

# Approach Two
#2: In case you dont have the head node, and just the node itself, its best to copy data from the next node onto our node..
current.data = current.next.data
current.next = current.next.next

So we basically delete current.next by copying it to our node since we dont have the previous nodes..


'''