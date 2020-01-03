'''
Question: 2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
SOLUTION
as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C -> D -> E -> C[thesameCasearlier] Output: C

Thoughts: Easy to do with a hashmap, keep traversing and as soon as you find a duplicate, you can point out. 

Without hashmap? Thinking of a runner method.. Fast runner and slow runner.. 

Solution: They both must collide at k nodes before start of loop.. 
this is also k node from start of loop.. so can find out the starting loop.

# Initialize..
SLOW = SELF.HEAD;
FAST = SELF.HEAD;

# Update in the loop..
SLOW = SLOW.NEXT
FAST = FAST.NEXT.NEXT


'''