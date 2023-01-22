"""
Queue is first in first out data structure.
To implemement a queue, we use a dynamic array.
Queue has main two operations: enqueue and dequeue.
Enqueue: appends new item to the queue.
Dequeue: removes the first element on the queue.
"""

class Queue:
    def __init__(self):
        self.queue = []

    # Add new element to the queue
    def enqueue(self, item):
        self.queue.append(item)

    # Remove the first element from the queue
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # find the length of the queue
    def queue_Len(self):
        return len(self.queue)

    # Display queue
    def print_queue(self):
        print(self.queue)

# Test

q = Queue()


q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print_queue()
q.dequeue()
print("Removing the first element from the queue")

q.print_queue()