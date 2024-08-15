'''
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

'''

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val 
        self.prev, self.next = None # prev and next node make it doubly linked list

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to Node

        # left = LRU(1,1) <-> right = (2,2)MRU
        self.left, self.right = Node(0, 0), Node(0, 0) # keep track of LRU node (left) and MRU node (right)
        self.left.next, self.right.prev = self.right, self.left # doubly linked list pointing to each other


    # remove node from doubly linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next 
        node.prev, node.next  = nxt, prev

    
    # insert node at right (most recently used)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node 
        node.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove key from cache and insert to right ; so that we know it's most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the doubly linked list and delete the LRU from the cache
            lru = self.left.next
            self.remove(lru) # remove from linked list
            del self.cache[lru.key]


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)