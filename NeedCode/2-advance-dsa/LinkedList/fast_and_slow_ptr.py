'''
Fast and Slow pointers in Linked List

- See below function defined under class with can be achieved by Fast and Slow pointer :
    - middleOfList
    - 


'''

# Find the middle of a linked list with two pointers.
# Time: O(n), Space: O(1)
def middleOfList(self):
    slow, fast = self.head.next, self.head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val     

# Determine if the linked list contains a cycle.
# Time: O(n), Space: O(1)
def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False



# Determine if the linked list contains a cycle and
# return the beginning of the cycle, otherwise return null.
# Time: O(n), Space: O(1)
def cycleStart(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    # make sure there is cycle exist otherwise return None
    if not fast or not fast.next:
        return None
    
    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow # Head of the Node where cycle start

