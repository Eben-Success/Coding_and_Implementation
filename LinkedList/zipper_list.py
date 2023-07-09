# Question https://structy.net/problems/zipper-lists
# Time O(min(n, m): n: len(n) & m: len(m)
# Space O(1)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def zipper_list(head_1, head_2):
    tail = head_1
    current_1 = head_1.next
    current_2 = head_2.next
    count = 0

    while current_1 is not None and current_2 is not None:
        if count % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next
        tail = tail.next

        if current_1 is not None:
            tail.next = current_1
        if current_2 is not None:
            tail.next = current_2

    count += 1
    return head_1


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
    a = zipper_list(a, b)
    print(a)
