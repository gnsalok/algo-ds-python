
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while(curr):
            nextNode = curr.next
            curr.next = prev 
            prev = curr
            curr = nextNode
        return prev


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

    curr = newHead
    while(curr):
        print(curr.val)
        curr = curr.next

        