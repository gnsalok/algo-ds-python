'''
N Queen Problem
'''

queen = [-1] * 8 # queen[i] -> where is my queen in row i
n = 8

def rec(level): # rec -> no. of ways to populate [level  ... n-1] row for a valid configuration
    # level -> row in which we are placing the queen

    # pruning 


    # base case
    if level == n:
        # if you reach to Nth level, everything above is valid solution
        return 1 

    # COMPUTE
    # explore all choices
    # if choice is valid
    # make that choice

    ans = 0

    # loop over all the choices
    for col in range(n):
        # check if choice is valid
        if check(level, col):
            # make the choice ; here, place the queen
            queen[level] = col

            # explore the option
            ans += rec(level+1)

            # revert placing the queen (backtracking)
            queen[level] = -1
    return ans


def check(row, col):
    for i in range(row):
        prow = i
        pcol = queen[i]

        if (pcol == col) or (abs(col - pcol) == abs(row - prow)):
            return False
    return True
        


print(rec(0))