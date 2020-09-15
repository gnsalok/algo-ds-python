"""
Stack implementation in Python
Logic:
   - Take a list as base data structure
   - Push item to end using list's append method.
   - Pop item, but returning the last item and deleting it.
   - Peek item but returning the last item
   
Author : Alok Tripathi
"""


class Stack:
    """ Stack in Python """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        """ check if stack is empty"""
        return self.items == []

    def push(self, item):
        """ Add new item to stack"""
        self.items.append(item)

    def pop(self):
        """ Remove item from stack """
        item = self.items[len(self.items)-1]
        del self.items[len(self.items)-1]
        return item

    def peek(self):
        """ Return last item without removing"""
        return self.items[len(self.items)-1]

    def size(self):
        """ return size of the stack"""
        return len(self.items)-1


if __name__ == "__main__":
    st = Stack()
    print(st)

    print(st.isEmpty())

    for i in range(0, 10):
        st.push(i)

    print(st.size())
    print(st.pop())
    print(st.size())
    print(st.peek())
    print(st.size())
    print(st.isEmpty())
