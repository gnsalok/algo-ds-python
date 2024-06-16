'''

'''


    # one more solution
    one_step = 1
    two_step = 2

    for i in range(2, n):
        temp = two_step
        next_step = one_step + two_step
        two_step = next_step
        one_step = temp
    return two_step