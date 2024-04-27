class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head
    
    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
    
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
        
    def print(self):
        curr = self.head
        while curr:
            print(curr.val, " -> ", end="")
            curr = curr.next
        print()


ll = LinkedList()



ll.insertEnd(1) # 0th node
ll.insertEnd(2) # 1st node
ll.insertEnd(3) # 3rd node

ll.remove(1)

ll.print()

print(ll.tail.val)