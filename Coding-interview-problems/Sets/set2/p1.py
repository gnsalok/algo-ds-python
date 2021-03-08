class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # initially it's pointing to None (Object reference)


class LinkedList:
    def __init__(self):
        self.head = None

    def listLength(self):
        currNode = self.head
        length = 0
        while currNode is not None:
            length += 1
            currNode = currNode.next
        return length

    def insertEnd(self, newNode):
        ''' Inserting Node in the End '''
        if self.head is None:
            self.head = newNode
        else:
            # Making copy for traversal
            lastNode = self.head

            # Traversing list to last node and advancing the list
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertHead(self, newNode):
        ''' Inserting Node as a head node '''
        # Creating TempNode to store the reference of the list
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def insertAt(self, newNode, pos):
        ''' Inserting Node at desired position '''
        currNode = self.head
        currPos = 0

        if pos < 0 or pos > self.listLength():
            print("Invalid Position")
            return

        while True:
            if currPos == pos:
                previousNode.next = newNode
                newNode.next = currNode
                break
            previousNode = currNode
            currNode = currNode.next
            currPos += 1

    def reverse(self):
        ''' Function to reverse the linked list - Iterative approach'''
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printList(self):
        '''Showing the list'''
        # Checking list is empty
        if self.head is None:
            print("List is empty")
            return

        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None


# Driver program
if __name__ == "__main__":

    firstNode = Node(20)
    linkedList = LinkedList()
    linkedList.insertEnd(firstNode)

    secondNode = Node(30)
    linkedList.insertEnd(secondNode)

    thirdNode = Node(10)
    linkedList.insertHead(thirdNode)

    # Passing data along with index
    fourthNode = Node(15)
    linkedList.insertAt(fourthNode, 1)

    linkedList.reverse()

    linkedList.printList()
