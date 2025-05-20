'''
You have skill and time a input array. 

time = [3, 5, 4, 2, 1]
skill = [3, 4, 1, 3, 1]

conditions
x = 6 # skill you case learn
k = 2 # in 2 no. of problems

Find the maximum skill you can get?

'''

# TODO : Need to run and give example

def rec(level, time_taken, item_taken, cache={}):
    '''
    max skill I can make from [level...n-1] if [0...level-1 is decided]... parameteres mean from [0...level-1
    
    '''

    # Pruning (out bound check - not required here)

    # base case : min/max problem then it's return 0
    if level == n:
        return 0
    
    # cache check
    if (level, time_taken, item_taken) in cache:
        return cache[(level, time_taken, item_taken)]


    # compute / transition
    ans = rec(level+1, time_taken, item_taken)

    # check
    if time_taken + time[level] <= x and item_taken + 1 <= k:
        # move
        cache[(level, time_taken, item_taken)] = min(ans, skill[level] + rec(level + 1, time_taken + time[level], item_taken + 1, cache))

    # save and return
    return cache[(level, time_taken, item_taken)]

    

# example 1
time = [3, 5, 4, 2, 1]
skill = [3, 4, 1, 3, 1]
x = 6
k = 2
n=0