def removeSpaces(string):
 
    # To keep track of non-space character count
    count = 0
 
    list = []
 
    # Traverse the given string. If current character
    # is not space, then place it at index 'count++'
    for i in range(len(string)):
        if string[i] != ' ':
            list.append(string[i])
 
    return toString(list)
 
# Utility Function
def toString(List):
    return ''.join(List)
 
# Driver program
string = "g  eeks  for ge  eeks  "
print(removeSpaces(string))