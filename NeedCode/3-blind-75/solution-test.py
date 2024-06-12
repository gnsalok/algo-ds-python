 ans = ListNode(0)
        ans.next = head
        
        first = ans 
        second = ans 
        
        #break on 2th index for first time & maintain N gap b/w both pointers
        for i in range(0, n+1):
            first = first.next
        
        while(first is not None):
            first = first.next
            second = second.next
            
        second.next = second.next.next

        return ans.next
    