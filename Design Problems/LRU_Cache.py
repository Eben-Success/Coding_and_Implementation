"""
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

"""
Clarifying Questions
1. What are we caching?
2. Can we assume inputs are valid?
3. Can we assume the inputs fit into memory.
4. What is the maximum size of our capacity?
5. Range of key?
6. Range of value?
7. How many calls will be made to our API?
"""

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = ListNode(-1, -1) # Least Recently Used Cache
        self.right = ListNode(-1, -1) # Most Recently Used Cache

        # set the pointers
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove_node(node)
        self.insert_node(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.remove_node(old_node)

        node = ListNode(key, value)
        self.insert_node(node)
        self.cache[key] = node

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove_node(lru)
            del self.cache[lru.key]

    def remove_node(self, node):
        """
        [left] <--> [prevNode] <--> [node] <-->[nextNode] <--> [right]
        
        """
        nextNode = node.next
        prevNode = node.prev

        nextNode.prev = prevNode
        prevNode.next = nextNode
        node = None
        

    def insert_node(self, node):
        """
        [left] <--> [prevNode] <--> [node] <--> [NEWNODE]<--> [right]
        
        """
        prevNode = self.right.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = self.right
        self.right.prev = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)