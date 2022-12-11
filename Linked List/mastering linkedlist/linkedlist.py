class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def push(self, new_node):
        new_node = Node(new_node)
        # make the next of the new node as head
        new_node.next = self.head
        # move the head to point new node
        self.head = new_node
        
    def insert_after(self, prev_node, new_node):
        if prev_node is None:
            return 
        
        new_node = Node(new_node)
        # make the next of the new node as the next of the prev_node
        new_node.next = prev_node.next
        prev_node.next = new_node
        
        
    def append(self, new_node):
        new_node = Node(new_node)
        
        # if linkedlist is empyt, make the new node head
        if self.head is None:
            self.head = new_node
            return 
        
        # Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
        