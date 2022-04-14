'''
WIP 
                  1

          2                 3.   
    4          5        6       7
8      9   10    11


OP - 1, 2, 3, 4,6,7, 8,9,10,11
*/

''' 


def printBoundary(root):
    be = []
    queue = []
    queue.append(root.val)
    
    while(queue):
        cur = queue.pop(0)
        
        if(i == 0):
            be.append(cur.val)
        
        if(root.left is None and root.right is None):
            be.append(cur.val)
            
        printBoundary(root.left)
        printBoundary(root.right)
            
        
        
        
        
        
        