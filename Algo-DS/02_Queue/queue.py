"""
Queue Implementation in Python.
Author : Alok Tripathi
"""


class Queue:
    def __init__(self, n):
        self.data = [None]*n
        self.front = -1
        self.rear = -1
        self.size = n

    def is_empty(self):
        """ To check if Queue is empty"""
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def is_full(self):
        """ Check if queue is full"""
        if self.rear == self.size-1:
            return True
        return False

    def enqueue(self, item):
        """Add a element into the queue"""

        # is queue full?
        if self.is_full():
            print("queue is full")
            return False

        # is queue empty?
        elif self.is_empty():
            self.rear = 0
            self.front = 0

        else:
            self.rear = (self.rear+1) % self.size

        self.data[self.rear] = item

    def dequeue(self):
        """ Remove item from the front."""

        # is queue empty?
        if self.is_empty():
            print("queue is empty")
            return None

        # only one item in the queue
        elif self.front == self.rear:
            item = self.data[self.front]
            self.front = -1
            self.rear = -1
            return item

        else:
            item = self.data[self.front]
            self.front = (self.front + 1) % self.size
            return item

    def peek(self):
        """ return the first item of the queue without removing it."""

        # is queue empty?
        if self.is_empty():
            return None
        else:
            return self.data[self.front]

    def length(self):
        """ Find length of the queue"""

        # is queue empty?
        if self.front == -1 and self.rear == -1:
            return 0
        else:
            l = (self.rear - self.front) + 1
            return l

    def display(self):
        """ Display queue items"""

        # is queue empty?
        if self.is_empty():
            return None

        q = ""
        s = self.front
        e = self.rear
        for i in range(s, e+1):
            q = q + str(self.data[i]) + " --> "

        return q


if __name__ == "__main__":
    qu = Queue(5)
    print(qu)
    print("Is queue empty? " + str(qu.is_empty()))
    print("Is queue Full? " + str(qu.is_full()))
    print("Length of the queue ? " + str(qu.length()))
    for i in range(5, 10):
        qu.enqueue(i)

    print("Queue -- " + qu.display())
    print("Peek Item ---" + str(qu.peek()))
    print('*' * 30)
    print(qu.dequeue())
    print(qu.dequeue())
    print(qu.dequeue())
    print(qu.dequeue())
    print(qu.dequeue())
    print(qu.length())
    print(qu.display())
    print('*' * 30)
    qu.enqueue(100)
    print(qu.length())
    print(qu.display())
    qu.enqueue(100)
    print(qu.length())
    print(qu.display())
