# Time O(n)
# Space O(1)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def sum_list(head):
    if head is None:
        return 0
    return head.val + sum_list(head.next)

x = Node(38)
y = Node(4)

x.next = y

print(sum_list(x))

