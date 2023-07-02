'''
Merge two sorted list and contains duplicate elements.

TO :  O(M+N)

'''

def nextGap(gap):
    if(gap <= 1):
        return 0
    return gap//2 + gap%2  # get the ceil 

# TODO 
def mergeTwoSortedList(l1, l2, m, n):
    m = len(l1) 
    n = len(l2)
    g = m + n 

    gap = nextGap(g)





  



    
    


if __name__ == "__main__":
    l1 = [1,2,4]
    l2 = [1,3,4]

    mergeTwoSortedList(l1, l2)

    # ans = mergeTwoSortedList(l1, l2)
    # print(ans)  # 1,1,2,3,4,4
