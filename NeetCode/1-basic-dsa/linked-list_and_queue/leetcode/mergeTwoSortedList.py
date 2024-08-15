'''
https://leetcode.com/problems/merge-two-sorted-lists/

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
            
        return dummy.next
