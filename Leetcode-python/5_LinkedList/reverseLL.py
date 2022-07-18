'''
1,2,3,4,5
5,4,3,2,1

'''


#Definition for singly-linked list.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def reverseList(self, head):
        if(head is None):
            return []
        
        helper = None

        while(head is not None):
            nextNode = head.next
            head.next = helper   # make backward link
            helper = head
            head = nextNode 
        return helper


head = Node(1)
sn = Node(3)
tn = Node(5)
fon = Node(2)
fvn = Node(4)

head.next = sn
sn.next = tn
tn.next = fon
fon.next = fvn

sl = Solution()

answer = sl.reverseList(head)
# print(answer.val)

while(answer is not None):
    if(answer.val == 1):
        print(answer.val)
    else:
        print(answer.val, end="=>")
    answer = answer.next

            
        