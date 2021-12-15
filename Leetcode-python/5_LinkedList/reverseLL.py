'''
1,2,3,4,5
5,4,3,2,1

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None):
            return []
        
        helper = None
        while(head is not None):
            nextNode = head.next
            head.next = helper
            helper = head
            head = nextNode 
        return helper
            
        