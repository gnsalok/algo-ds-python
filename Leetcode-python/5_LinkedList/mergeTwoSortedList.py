'''
List 1 : 1 -> 3 -> 4
List 2 : 1 -> 2 -> 6

Final : 1,1,2,3,4,6
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # cur is moving pointer and represent newly created two merged list
        # ans is pointing to head
        cur = ListNode(0)
        ans = cur
        
        while(list1 and list2):
            if(list1.val > list2.val):
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next

            cur = cur.next
        
        while(list1):
            cur.next = list1
            list1 = list1.next
            cur = cur.next
            
        while(list2):
            cur.next = list2
            list2 = list2.next
            cur = cur.next
        
        return ans.next


if __name__ == "__main__":
    l1 = [1,2,4]
    l2 = [1,3,4]

    
            
                