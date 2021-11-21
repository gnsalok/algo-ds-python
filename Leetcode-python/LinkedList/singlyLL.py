'''
Singly Linked List
'''
import ctypes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    # Display the List 
    def printList(self):
        temp = self.head # Create a temp Node
        linked_list = []
        while(temp):
            linked_list.append(temp.data)
            temp = temp.next
        print(linked_list)

    # Insert a Node at pos in the list 
    def insertNode(self, val, pos):
        target = Node(val)
        
        if(pos == 0):
            target.next = self.head  # Create a link
            self.head = target  # Make target as Head Node
            return 
        
        #returns previous node where your want to insert the value
        def getPre(pos):
            temp = self.head
            count = 1
            while(count < pos):
                temp = temp.next
                count += 1
            return temp 
        
        prev = getPre(pos)
        nextNode = prev.next
        prev.next = target
        target.next = nextNode

    # Delete an element from List
    def deleteEle(self,key):
        temp = self.head
        if(temp is None):
            return 

        # Head Node deletion case     
        if(temp.data == key):
            self.head = temp.next
            temp = None 
            return 
        
        while(temp.next.data != key):
            temp = temp.next
        
        target_node = temp.next
        temp.next = target_node.next # Making the link 
        target_node.next = None 

    

if __name__ == "__main__":
    #singly linked list 
    sll = LinkedList()

    # setting head to 5  :: head is Node -> data is 5, next is None 
    sll.head = Node(5)

    print(sll.head.data)   # Print Data at head 
    print("Initial Head Node Pointer ",sll.head.next)
     
    # Creating Nodes 
    second_node = Node(10)
    third_node = Node(11)
    fourth_node = Node(12)

    # Pointing Nodes 
    sll.head.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node

    # Insert ele in the node at pos
    sll.insertNode(123,2)
    sll.insertNode(111,0)
    sll.insertNode(345,1)

    # Print the list 
    sll.printList()

    sll.deleteEle(123)
    sll.printList()







    



        