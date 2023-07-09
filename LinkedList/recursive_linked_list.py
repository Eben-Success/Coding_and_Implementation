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

def print_linked_list_recursive(head):
    if head == None:
        return
    print(head.val)
    return print_linked_list_recursive(head.next)

print(print_linked_list_recursive(a))


