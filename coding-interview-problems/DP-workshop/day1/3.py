'''
TODO: Fix this code. passing t,s to rec.

Note: When you are dealing with min/max problem ; go with return 0 as base case.

You have skill and time a input array. 

time = []
skill = []

conditions
x = 6 # skill you case learn
k = 2 # in 2 no. of problems

Find the maximum skill you can get?

Note : you can solve this problem using DP without explicitly using "check" function.
'''

n = 0 # TODO: check 
taken = [False] * 20
def rec(level): # max skill I can make from current [level...n-1]
    # level -> current item in [0... n-1]
    
    # pruning 

    # base 
    if level == n:
        return 0

    # compute
    # loop over choice


    # choice 1 :don't take the item (skip)
    ans = rec(level + 1)

    # choice 2 : take the item

    if(check(level)):
        # place the change and move (take the item)
        taken[level] =  True
        #move
        ans = max(ans, s[level] + rec(level+1)) # max in [level+1...n]
        #revert
        taken[level] = False


    # return
    return ans


# check if we can take the item or not
def check(level):
    timeTaken = 0
    itemTaken = 0

    for i in range(level):
        if taken[i]:
            timeTaken += t[i]
            itemTaken += 1
    
    timeTaken += t[level]
    itemTaken += 1

    if itemTaken <= x and itemTaken <= k:
        return True
    else:
        return False


        





# example 1
time = [3, 5, 4, 2, 1]
skill = [3, 4, 1, 3, 1]
x = 6
k = 2

# answer 3 + 3 skill = 6 ; no. of problems = 2


