class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def zipper_list_recursive(head1, head2):
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return None
    if head2 is None:
        return None

    next1 = head1.next
    next2 = head2.next
    head1.next = head2
    head2.next = zipper_list_recursive(next1, next2)
    return head1


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

x = Node("x")
y = Node("y")
z = Node("z")

x.next = y
y.next = z

if __name__ == '__main__':
    a = zipper_list_recursive(a, b)
    print(a)

