from queue import Queue

queue = Queue(maxsize=5)

print(queue.qsize())

queue.put('a')
queue.put('b')
queue.put('c')

print(queue.get())
print(queue.get())
print(queue.get())


print("\nFull ->",queue.full())
print("\nEmpty ->",queue.empty())


