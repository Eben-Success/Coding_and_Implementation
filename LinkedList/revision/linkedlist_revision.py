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
        """
        Initialize a new variable called temp and
        use it to traverse the node printing its
        values.
        """
        temp = self.head;
        
        while temp is not None:
            print(temp.val, "-->", end="")
            temp = temp.next
        print("End")

    def insert_last(self, val):
        # Time: O(1)
        # create a new node
        node = Node(val)

        # if Linkedlist is empty, insert at first
        if self.tail is None:
            self.insert_first(val)
            return

        self.tail.next = node
        self.tail = node

        self.size += 1

    def insert_at_index(self, index, val):
        # if the index == 0
        # else: traverse the linkedlist to index - 1
        # if not found: raise IndexError
        # else: insert at that index

        node = Node(val)
        if index == 0:
            node.next = self.head
            self.head = node

        else:
            cur = self.head
            count = 0

            while cur and count < index - 1:
                cur = cur.next
                count += 1

            if cur is None:
                raise IndexError("Index not Found")
            
            cur.next = node.next
            node.next = cur.next

            



        
        
        
        
        
            
            
list = LinkedList()
list.insert_first(3)
list.insert_first(5)
list.insert_first(7)
list.insert_first(9)
list.insert_first(11)
list.insert_first(12)
list.insert_first(56)
list.insert_first(63)
list.insert_last(99)
list.insert_at_index(3, 100 )
list.display_node()


        
            
            
        

        
        