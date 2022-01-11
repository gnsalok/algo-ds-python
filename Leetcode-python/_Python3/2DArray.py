
# Always do with for loop other instea doing "*", it will not place your input in correct position. 

row, col = (4,3)
arr = [ [0]*col for i in range(row) ]
print(arr)


'''
Check this out as  well
Res : [0,0,0,0,0][0,0,0,0,0][0,0,0,0,0]
'''
matrix = [[0 for x in range(5)]
            for y in range(3)]
matrix[1][1] = 1
print(matrix) 


'''
Creating bucket
[[], [], []]
'''

bucket = [[] for _ in range(3)]
print(bucket) 




'''
Not Recommended 
'''
row, col = (3,4)
# arr = [[0]*col] * row 
# print(arr)