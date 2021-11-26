


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        temp = self.head
        ll = []

        while(temp):
            ll.append(temp.data)
            temp = temp.next
        print(ll)

    def insertAtPos(self, val, pos):
        target = Node(val)

        while(pos == 0):
            target.next = self.head
            self.head = target
            return
        
        def getPos(pos):
            temp = self.head
            count = 1
            if(count < pos):
                temp = temp.next
                count += 1
            return temp 
        
        pre = getPos(pos)
        nextNode = pre.next
        pre.next = target
        target.next = nextNode

    def deleteNode(self, key):
        temp = self.head
        
        #LL in empty
        if(temp is None):
            return 


        # CASE : Head Node Deletion 
        if(temp.data == key):
            self.head = temp.next
            temp = Node

        #Case : Delete in the middle
        while(temp.next.data != key):
            temp = temp.next
        
        targetNode = temp.next
        temp.next = targetNode.next
        targetNode.next = None


        




    



if __name__ == "__main__":
    print("Linked List Representation")
    ll = LinkedList()
    ll.head = Node(4)

    second_node = Node(5)
    ll.head.next = second_node

    third_node = Node(6)
    second_node.next = third_node

    ll.insertAtPos(5,0)
    ll.insertAtPos(10,6)

 
    ll.deleteNode(6)
    

    ll.display()


