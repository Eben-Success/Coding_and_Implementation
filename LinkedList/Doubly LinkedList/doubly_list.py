from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def prepend_node(self, val: int) -> None:
        # insert at the front if node is not none
        
        newNode = Node(val)
        
        