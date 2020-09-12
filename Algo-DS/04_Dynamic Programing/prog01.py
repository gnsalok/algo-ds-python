''' Check if a list can be partitioned on not
Given:
   1. list of positive intergers.
   2. Any size.

Output:
   1. check if list can be partitioned such that sum of elements in
   both the partitions is same.

Logic:
   1. find the sum of intergers in list.
   2. if sum is odd, then list can be partitioned. Return false example, if sum is 7, we can't have
   two lists with sum as 3.5 and 3.5.
   3. If sum is even, try to find the subset with total as sum/2
'''

def find_sum(l):
    s = 0
    for i in l:
        s = s + i
    return s

def is_subset(l, n, s ):
    if s == 0:
        return True
    elif n == 0 and s > 0:
        return False

    if l[n-1] > s:
        return is_subset(l, n-1, s)
    
    return is_subset(l, n-1, s) or is_subset(l, n-1, s - l[n-1])
    


if __name__ =='__main__':
    l = [1, 2, 3, 8]
    partitioned = False

    s = find_sum(l)
    print('Sum - ', s)
    if s % 2 == 0:
        half_sum = s//2
        partitioned = is_subset(l, len(l), half_sum)

    if partitioned:
        print('List can be partitioned')
    else:
        print('List can not be partitioned')



