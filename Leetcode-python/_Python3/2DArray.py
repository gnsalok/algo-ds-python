
# Always do with for loop other instea doing "*", it will not place your input in correct position. 

row, col = (4,3)
arr = [ [0]*col for i in range(row) ]
print(arr)


'''
Check this out as  well
Res : [0,0,0,0,0][0,0,0,0,0][0,0,0,0,0]
'''
matrix = [[[] for col in range(5)]
            for row in range(3)]

print(matrix)
for i in range(3): # row 
    for j in range(5): # col
        print(matrix[i][j])

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