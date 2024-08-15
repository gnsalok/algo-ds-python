from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy 

        while list1 and list2:
       
            if list1.val < list2.val:
                tail.next = list1
                # update ptr for next value to check
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # assume in both list any list contains more nodes
        # you just take the list and attach to the tail
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        # DEBUG: dummy points to head
        #print(dummy.next)
    
        return dummy.next
    

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)


l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


list1 = [l1, l1.next,l1.next.next]
list2 = [l2, l2.next,l2.next.next]

sl = Solution()

node = sl.mergeTwoLists(list1, list2)


while node:
    print(node.val)
    node = node.next