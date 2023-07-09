class Node:
    def __init__(self, val):
        self.val = val
        self.next = next
        
class Linkedlist:
    def __init(self):
        self.head = None
        
        # insert new node at the beginning
        def push(self, new_node):
            new_node = Node(new_node)
            new_node.next = self.head
            self.head = new_node
            
        def deleteNode(self, key):
            
            # store head node
            cur = self.head
            
            # if head node itself holds the key to be deletec
            if cur is not Node:
                if cur == key:
                    self.head = cur.next
                    cur = None
                    return 
                
            # search the key to be deleted
            # keep track of its previous node as we need
            # to change its prev.next
            
            while cur is not None:
                if temp.val == key:
                    break
                prev = cur
                cur = cur.next