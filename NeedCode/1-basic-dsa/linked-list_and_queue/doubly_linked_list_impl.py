class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

'''
Tip:
Draw -> Visualize -> Code 
'''
class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)

        # connect left and right nodes to make insertion and deletion easier 
        self.left.next = self.right
        self.right.prev = self.left
        
    
    def get(self, index: int) -> int:
        curr = self.left.next

        while curr and index > 0:
            curr = curr.next
            index -= 1
        # if index == 0 means we are able to reach position where we want to reach
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1
        
    
    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        # similar to addAtHead -> just get next, prev from right pointer
        node, next, prev = ListNode(val), self.right, self.right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev


    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next 

        while curr and index > 0:
            curr = curr.next
            index -= 1
        # if index == 0 means we are able to reach position where we want to reach
        if curr and index == 0:
            node, prev, next = ListNode(val), curr.prev, curr
            prev.next = node 
            next.prev = node
            node.next = curr
            node.prev = prev


    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next 

        while curr and index > 0:
            curr = curr.next
            index -= 1

        # if index == 0 means given index is preset so not able to add
        if curr and curr != self.right and index == 0:
            prev, next =  curr.prev, curr.next

            prev.next = curr.next 
            next.prev = prev


          
        


# Your MyLinkedList object will be instantiated and called as such:

# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)