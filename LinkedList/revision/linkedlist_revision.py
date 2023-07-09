class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def insert_first(self, val):
        # create a new node
        node = Node(val)
        
        # point the new node to the head
        node.next = self.head
        self.head = node
        
        # if the new node if the first node created,
        # then tail should also point to the new node
        if self.tail is None:
            self.tail = self.head
        
        self.size += 1
        
        
    def display_node(self):
        """Initialize a new variable called temp and
        use it to traverse the node printing its
        values.
        """
        temp = self.head;
        
        while temp is not None:
            print(temp.val, "-->", end="")
            temp = temp.next
        print("End")
        
        
        
        
            
            
list = LinkedList()
list.insert_first(3)
list.insert_first(5)
list.insert_first(7)
list.insert_first(9)
list.insert_first(11)
list.insert_first(12)
list.insert_first(56)
list.insert_first(63)
list.display_node()


        
            
            
        

        
        