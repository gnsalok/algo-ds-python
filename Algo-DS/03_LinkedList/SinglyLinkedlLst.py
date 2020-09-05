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
        self.next = None  # initially it's pointing to None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            # making copy for traversal
            lastNode = self.head

            # traversing list to last node and advancing the list
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):

        # if list is empty
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
    linkedList.insert(firstNode)

    secondNode = Node("Akhil")
    linkedList.insert(secondNode)

    thirdNode = Node("Eklavya")
    linkedList.insert(thirdNode)

    linkedList.printList()
