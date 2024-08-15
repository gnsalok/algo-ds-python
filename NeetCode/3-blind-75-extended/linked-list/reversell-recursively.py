
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Recursive solution to reverse the linked list
    def reverseList(self, head):
        
        if not head:
            return None 
        
        newHead = head 
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None


        


if __name__ == "__main__":   

    head = ListNode(1)
    sn = ListNode(2)
    tn = ListNode(3)
    fon = ListNode(4)
    fvn = ListNode(5)

    head.next = sn
    sn.next = tn
    tn.next = fon
    fon.next = fvn

    sl = Solution()
    newHead = sl.reverseList(head)

        