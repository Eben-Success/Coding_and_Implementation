class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    # add the end of the linkedlist
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return 
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # add to the begining of the linkedlist
    def prepend(key, data):
        pass