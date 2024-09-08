'''
Find Cycle in the List.
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        turtle = head
        
        while(turtle and hare and hare.next):
            hare = hare.next.next
            turtle = turtle.next
            
            if(turtle == hare):
                return True
        
        return False
            