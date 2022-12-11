# Traverse linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def traverse(head):
        cur = head
        while cur != None:
            print(cur.val)
            cur = cur.next
            
           
           
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d
q = Node.traverse(a)
print(q)