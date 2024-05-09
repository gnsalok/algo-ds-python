'''
leftChild of i = heap[2 * i]
rightChild of i = heap[(2 * i) + 1] 
parent of i = heap[i // 2]
'''


# Min Heap
class Heap:
    def __init__(self):
        # 0 is dummy, not considered
        self.heap = [0]

    '''
    log N
    '''
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        # Percolate up
        # if parent is greater than swap
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

    # pop is bit complicated but try to visualize and dry run
    '''
    log N
    '''
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        # store root node (min value) for return
        res = self.heap[1]   
        # Move last value to root
        self.heap[1] = self.heap.pop()
        i = 1
        # Percolate down
        # util there is no left child exist
        while 2 * i < len(self.heap):
            # do we also have right child? (checking in build head array)
            if (2 * i + 1 < len(self.heap) and 
            self.heap[2 * i + 1] < self.heap[2 * i] and 
            self.heap[i] > self.heap[2 * i + 1]):
                # Swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # Swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            # if left and right child contains greater value / proper position; exit from the loop
            else:
                break
        return res

    def top(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    '''
    TC: O(N) 

    Reason:
    - percolating down is more efficient than percolating up.
    - In perc. down, we have (n-1) nodes in to sift down, but 
    - In perc. up all the node to sift up (n+1+...);
    which is worse.
    '''
    def heapify(self, arr):
        # 0-th position is moved to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            # Percolate down
            i = cur
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and 
                self.heap[2 * i + 1] < self.heap[2 * i] and 
                self.heap[i] > self.heap[2 * i + 1]):
                    # Swap right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    # Swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            # percolating each node in reverse order
            cur -= 1
