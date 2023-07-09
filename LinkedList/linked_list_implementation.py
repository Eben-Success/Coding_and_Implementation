class Node:
    def __init__(self, val, ):
        self.val = val
        self.next = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

# A -> B -> c -> D -> Null
# cur

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next

print_linked_list(a)

