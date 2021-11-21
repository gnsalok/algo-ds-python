from queue import LifoQueue

stack = LifoQueue()


print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')

print(stack.qsize())
print(stack.get())
