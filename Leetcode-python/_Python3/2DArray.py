
# Always do with for loop other instea doing "*", it will not place your input in correct position. 

row, col = (4,3)
arr = [ [0]*col for i in range(row) ]
print(arr)


'''
Not Recommended 
'''
row, col = (3,4)
# arr = [[0]*col] * row 
# print(arr)