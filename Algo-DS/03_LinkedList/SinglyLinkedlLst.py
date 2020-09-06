"""
Singly Linked List Implementation in Python
- Create a Node
- Create Linked List
- Add Node to linked list
- Print Values in Linked List 

Author : Alok Tripathi
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # initially it's pointing to None (Object reference)


class LinkedList:
    def __init__(self):
        self.head = None

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

    def printList(self):

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


# Driver program
if __name__ == "__main__":

    firstNode = Node("Alok")
    linkedList = LinkedList()
    linkedList.insertEnd(firstNode)

    secondNode = Node("Akhil")
    linkedList.insertEnd(secondNode)

    thirdNode = Node("Eklavya")
    linkedList.insertEnd(thirdNode)

    fourthNode = Node("Shefali")
    print(fourthNode)
    linkedList.insertHead(fourthNode)

    linkedList.printList()
