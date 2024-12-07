class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val 
        self.prev = self.next = None  # prev and next node pointers for the doubly linked list

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to Node

        # Initialize the LRU and MRU dummy nodes
        self.left, self.right = Node(0, 0), Node(0, 0)  
        self.left.next, self.right.prev = self.right, self.left  # doubly linked list pointing to each other

    # remove node from doubly linked list (For DLL operation)
    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next = nxt
        nxt.prev = prev

    # insert node at right (most recently used) (; for DLL operation)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node 
        node.prev = prev 
        node.next = nxt
        nxt.prev = node
    
    # GET will get the element and update the position of node with REMOVE and RE-Insert
    def get(self, key: int) -> int:
        if key in self.cache:
            # remove key from cache and insert to right ; so that we know it's most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    # PUT will store the value if not already present AND if capacity is reached then it will evict from the cache
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the doubly linked list and delete the LRU from the cache
            lru = self.left.next  # LRU node is the one right after the left dummy node
            self.remove(lru)  # remove from linked list
            del self.cache[lru.key]
