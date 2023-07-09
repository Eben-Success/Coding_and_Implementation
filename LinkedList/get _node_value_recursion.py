# Question: https://structy.net/problems/get-node-value
# Time O(n)
# Space O(1)

# Recursive Approach

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
                                    # 4
def get_node_value_recursive(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val
    return get_node_value_recursive(head.next, index-1)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value_recursive(a, 2))