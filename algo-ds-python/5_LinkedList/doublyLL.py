class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __int__(self):
        self.head = None

    def createList(self, arr):
        start = self.head
        n = len(arr)

        temp = start
        i = 0
        
        while(i < n):
            newNode = Node(arr[i])
            if(i == 0):
                start = newNode
                temp = start
            else:
                temp.next = newNode
                newNode.prev = temp 
                temp = temp.next 
            i += 1
        self.head = start
        return start
    
    def printList(self):
        temp = self.head
        linked_list = ""
        while(temp):
            linked_list += (str(temp.data) + " ")
            temp = temp.next
        print(linked_list)
        











if __name__ == "__main__":
    print("Doubly Linked List Implementation")

    arr = [5,1,3]
    dll = LinkedList()

    dll.createList(arr)
    dll.printList()


    

        
