class Node():
    def __init__(self, val):
        self.data = str(val)
        self.next = None

    def __str__(self):
        return self.data
    
class SinglyLinkedList():

    def __init__(self, val):
        node = Node(val)
        self.size = 1
        self.tail = node
        self.head = node

    ## Queue - Add at last 
    def add(self, val):
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1    

    ## Queue - Remove the first value
    def remove(self):
        temp_node = self.head
        self.head = self.head.next
        self.size -= 1
        return temp_node

    # Stack - Push on top
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1    

    # Stack - Pop the top one
    def pop(self):
        temp_node = self.head
        self.head = self.head.next
        self.size -= 1    
        return temp_node


    def __str__(self):
        output = ""
        count = 0
        node = self.head
        while(count<self.size):
            if count == self.size - 1:
                output += str(node)
            else:
                output += str(node) + " -> "
            node = node.next
            count += 1
        return output

if __name__ == "__main__":
    ## Queue
    slist = SinglyLinkedList(Node(4))
    slist.add(Node(5))
    slist.add(Node(6))
    print(slist)
    print(slist.remove()) # Removes the one added in the beginning in queue

    ## Stack
    slist = SinglyLinkedList(Node(4))
    slist.push(Node(5))
    slist.push(Node(6))
    print(slist)
    print(slist.pop()) # Removes the one added in the end in stack



    
