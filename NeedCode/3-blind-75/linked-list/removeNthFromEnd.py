'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

TC : O(N)
SC : O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy node and assign as left ptr so that we will be one node before which we want to delete
        dummy = ListNode(0, head) 
        left = dummy

        # make sure distance between left and right pointer in N (ie. 2)
        right = head

        while n > 0 and right:
            n -= 1
            right = right.next

        while right:
            left = left.next 
            right = right.next

        left.next = left.next.next

        return dummy.next

