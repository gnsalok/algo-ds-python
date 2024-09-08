'''
Immutable object is not pass by ref. Hence modification inside any func will not reflect in main scope.
'''

str = 'Alok'

def printMap(str):
    str = str + ' Tripathi'
    print("Inside func : ", str)

printMap(str)

print("Outside : ",str)




# Note : Above operation will change the main object if its immutable. ie : dict or list 