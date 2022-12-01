# QUEUE DATA STRUCTURE

Queue follows the First In First Out (FIFO) rule.

## Basic Operations of Queue
* Enqueue: add an element to the end of a queue.
* Dequeue: remove an element from the front of the queue.
* IsEmpty: check if queue is empty.
* Peek: Get the value of the front of the queue without removing it.

## Working of Queue
Queue operations work as follows:
* two pointers `FRONT` and `REAR`.
* `FRONT` track the first elemnent of the queue.
* `REAR` track the last element of the queue.
  * Initially, set value of `FRONT` and `REAR` to -1

## Complexity Analysis
The time complexity of enqueue and dequeue is O(1)
If we use the pop(n) in python, then the complexity becomes O(n) depending on the position of the item to be popped.

## Applications of Queue
* CPU scheduling, Disk Scheduling
* When data is transfered asynchronously between two processes. The queue is used for synchronization. For example: IO Buffers, pipes, file IO
* Handling of interrupts in real-time systems.
* Call Center phone systems use Queues to hold people calling them in order.