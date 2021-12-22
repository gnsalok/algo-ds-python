class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

    #Display the List
    def printList(self):
        tempNode = self.head 
        nodeValue = []

        while(tempNode):
            nodeValue.append(tempNode.data)
            tempNode = tempNode.next
        print(nodeValue)

    #Insert Node at Position
    def insertNodeAtPos(self, val, pos):
        target = Node(val)

        if(pos == 0):  # if pos is the first Node
            target.next = self.head
            self.head = target 
            return 

        def getPreviousNode(pos):
            temp = self.head
            count = 1
            while(count < pos):  # break this loop, when you will get the prev. node
                temp = temp.next  
                count += 1
            return temp

        preNode = getPreviousNode(pos)
        nextNode = preNode.next
        preNode.next = target
        target.next = nextNode

    
    #Deletion in list 
    def deleteNode(self, val):
        temp = self.head

        if(temp is None):
            return 
        
        if(temp.data == val):
            self.head = temp.next
            temp = None

        #Traverse till key
        while(temp.next.data != val):
            temp = temp.next
        
        target_node = temp.next
        temp.next = target_node.next # Making the link 
        target_node.next = None  # delete the link 





        






if __name__ == "__main__":
    sll = LinkedList()
    sll.head = Node(5)

    # Creating Nodes 
    second_node = Node(10)
    third_node = Node(11)
    fourth_node = Node(12)

    # Linking Nodes 
    sll.head.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node



    #calling LL function 
    sll.insertNodeAtPos(17,3)
    sll.printList()

    sll.deleteNode(17)
    sll.printList()


        

        

        