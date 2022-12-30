'''
--Time Complexity --
sift up and sift down : O(logN)

- Insertion -
By using sift down - O(N)
By using sift up - O(logN)

Author : Alok Tripathi
'''


class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # take last child child(means last ele) and apply formula (i-1)//2 to get the first parent
        firstParentIdx = (len(array) - 1 - 1) // 2
        for currIdx in reversed(range(firstParentIdx)):
            self.siftDown(currIdx, len(array)-1, array)
        return array

    def siftDown(self, currentIndex, endIdx, heap):
        childOneIdx = currentIndex * 2 + 1
        # break if reach at leaf 
        while(childOneIdx <= endIdx):
            childSecondIdx = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIdx else -1
            if(childSecondIdx != -1 and heap[childSecondIdx] < heap[childOneIdx]):
                idxToSwap = childSecondIdx
            else:
                idxToSwap = childOneIdx

            if(heap[idxToSwap] < heap[currentIndex]):
                self.swap(currentIndex,idxToSwap, heap)
                currentIndex = idxToSwap
                childOneIdx = currentIndex * 2 + 1
            else:
                break

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while(currentIdx > 0 and heap[currentIdx] < heap[parentIdx]):
            self.swap(currentIdx, parentIdx, self.heap)
            # if you swap currIdx <-> parentIdx, your currIdx should update with new node Idx
            # in order to calculate new parent
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] =  heap[j], heap[i]


if __name__ == "__main__":
    arr = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
    mhObj = MinHeap(arr)
    meanHeapArray = mhObj.buildHeap(arr)
    print("Mean Heap Array : ", meanHeapArray)
    