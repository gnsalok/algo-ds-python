'''
Think like programmer: [Recursion]https://www.youtube.com/watch?v=oKndim5-G94&t=0s

Problem :

Two int array representing sensor data. Sensor data array should be the same. but small difference. 

sensorA = [15,-4,56,10,23]
sensorB = [14,-9,56,14,23]

Expected : calculate absolute difference ?

absDiff = [1,5,0,4,0] = sumTotal -> 10

ie. : absolute diff between 10-14 = 4 [sensorA/B[3]]

'''


'''
3- Step to solve recursive problem : (Actual thinking in real world)

1. Write an iterative function to solve the problem.
    - Important that parameter list is correct
2. Write a "dispatcher" function. 
    - Function that solve problem on minimal dataset
        - In this case, when size parameter == 0 
    - Dispatcher call iterative function to handle non-minimal cases.
        - IMPORTANT: must pass smaller dataset to iterative function
            - In this case, passing size-1 for third parameter does the trick.
            - Means, Dispatcher must handle last element in the arrays.

3. In dispatcher, replace call to iterative function "totalDiff" with dispatcher function "totalDiffDispatcher" itself. (yay!! It's Recursive solution)



'''

# Not required anymore !!!
def totalDiff(arrA, arrB, size):
    totalDiff = 0
    for i in range(size):
        totalDiff += abs((arrA[i]) - (arrB[i]))
    return totalDiff

def totalDiffDispatcher(arrA, arrB, size):
    if size == 0: # for minimal dataset
        return 0
    lastElementDiff = abs(arrA[size-1] - arrB[size-1])
    diff = totalDiffDispatcher(sensorA, sensorB, size-1) + lastElementDiff
    return diff


sensorA = [15,-4,56,10,23]
sensorB = [14,-9,56,14,23]

# print(totalDiff(sensorA, sensorB, 5)) # expected 

print(totalDiffDispatcher(sensorA, sensorB, 5))

