class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    # add the end of the linkedlist
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return 
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    # add to the beginning of the linkedlist
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # insert after a node
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    # delete node
    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return 

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        pass

    def len_linkedlist(self):
        pass

    def swap_nodes(self, key_1, key_2):
        pass