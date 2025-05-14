'''
Similar to variation of climbing stairs problem.

---

how you write code while following template : level, choice, check, move

def rec(level):
    for (all choice):
        if check(valid choice):
            move(choice)

'''

n = 3
def rec(level): # Return -> no. of way to N if we are at stair level.
    # level -> stair I'm at

    # pruning : out of bound
    if level > n:
        return 0 # 0 element of counting problem

    # base case
    if level == n:
        return 1
    
    ans = 0
    # loop over choice
    for step in range(1, 3):
        # check -> if it's a valid choice
        if level + step <= n: # it means it's valid move
            ways = rec(level + step) # move
            ans += ways
    return ans # for this level


def solve():
    print(rec(1))

solve()





