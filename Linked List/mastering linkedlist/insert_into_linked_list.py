# Inserting into a linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
# Time: O(1)   
# Space: O(1)
# Add a node to the front of linked list

    def insert_infront(self, val):
        val= Node(val)
        val.next = self.head
        self.head = val
        

    # Add a node after a given node
    """
    1. First check if the given previous node is null.
    2. Allocate a new node
    3. Assign the data to the new node.
    4. Make the next of the new node as the next of the previous node.
    5. Move the next of the previous node as a new node.
    """
    
    # Time: O(1)
    # Space: O(1)
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            return
        new_data = Node(new_data)
        new_data.next = prev_node.next
        prev_node.next = new_data
        
        
        # Time: O(n)
        # Space: O(1)
        # Add a node at the end
        def insert_at_end(self, new_data):
            new_data = Node(new_data)
            
            # If the linked list is empty, make the 
           # new node as head
            
            if self.head is None:
                self.head = new_data
                return 
            
            # Else traverse till the last node
            last = self.head
            while last.next:
                last = last.next
            last.next = new_data
            
           
           
        
        
        
    
    
    
    
    
    
    
    
        
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

q = LinkedList.insert_infront("m")
print(q)

        