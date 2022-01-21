'''
Implement a circular queue.
'''


class Queue:
    def __init__(self, cap):
        self.cap = cap
        self.storage = [None] * cap
        self.head = 0
        self.tail = 0
        self.size = 0

    def isFull(self):
        return self.cap == self.size

    def enqueue(self, data):
        if(self.isFull()):
            raise Exception("Queue is Full.")
        self.storage[self.tail] = data
        self.tail += 1
        self.size += 1

    def dequeue(self):
        if(self.size == 0):
            return None

        data = self.storage[self.head]
        self.storage[self.head] = None
        self.head += 1

        # reset the queue
        if(self.head == self.tail):
            self.head = 0
            self.tail = 0

        self.size -= 1
        return data

    def Display(self):
        if(self.size == 0):
            return None

        for v in self.storage:
            print(v, end=" ")


if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print("Deque", q.dequeue())
    print("Deque", q.dequeue())

    q.Display()
