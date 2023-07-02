'''
1,2,3,4,5
5,4,3,2,1

TC : O(N) == SC
'''

#Definition for singly-linked list.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def reverseList(self, head):
        ans = []
        if(head is None):
            return []
        
        helper = None
        while(head is not None):
            nextNode = head.next
            head.next = helper   # make backward link
            helper = head
            head = nextNode 

        while(helper is not None):
            ans.append(helper.val)
            helper = helper.next
        return ans

# Driver
def main():
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
    print(answer)

# Main Calling
if __name__ == "__main__":
    main()

            
        