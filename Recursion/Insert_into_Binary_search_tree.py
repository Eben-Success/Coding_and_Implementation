

def insertNode(Node head, data):
    if head == None:
        head = Node();
        head.data = data
        return data
    
    if (data > head.data):
        head.right = insertNode(head.right, data)
    else:
        head.left = insertNode(head.left, data)
        
    return data