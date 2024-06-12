'''

https://leetcode.com/problems/reorder-list/

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next 

        # Step 1: Find the mid of the list using fast and slow ptr
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # second half of the list 

        slow.next = None # as it will be the last pointer ; edge case
        
        # Step 2 : Reverse the links of sencond half
        prev = None # hepler to reverse the list
        
        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode

        # Step 3: Merge the two halfs of the list
        first = head # start of the list
        second = prev # beginning of the second is prev (end of second half)

        while second:
            # as we are breaking the link 
            # first -> end, 
            tmp1, tmp2 = first.next, second.next
            first.next = second 
            second.next = tmp1

            #shifting the ptrs
            first = tmp1
            second = tmp2



