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
        curr = self.head # head is pointing to ListNode(-1) ; technically 0th node is -1 which needs to exclude

        '''
        NOTE :
        If index > 0 - means Linked List start count with 0 -> 0th Node = 1
        If index > 1 - means Linked List start with count 1 -> 1st Node = 1
        '''
        while  index > 1 and curr:
            index -= 1
            curr = curr.next
        # Remove the node ahead of curr
        # this will loop through one node before actual node at index
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
        
    def print(self):
        # skip dummy node
        curr = self.head.next
        while curr:
            print(curr.val, " -> ", end="")
            curr = curr.next
         


ll = LinkedList()



ll.insertEnd(1) # 1st node
ll.insertEnd(2) # 2nd node
ll.insertEnd(3) # 3rd node

ll.remove(1)

ll.print()