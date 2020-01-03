'''
Question: Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. 
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 
Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity, 
SetOfStacks. push() and SetOfStacks.popO should behave identically to a single stack (that is, p o p ( ) should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt ( i n t i n d e x ) which performs a pop operation on a specific sub- stack.


Thoughts: This looks straightforward, lets work on the pseudocode.

class StackSet:
    def push(val):
        currentStack = latestStack()
        if(currentStack.size < threshold):
            currentstack.push(val)
        else:
            new_stack = Stack()
            new_stack.push(val)
            stacks.add(stack)

    def pop():
        currentStack = latestStack()
        currentStack.pop()



'''