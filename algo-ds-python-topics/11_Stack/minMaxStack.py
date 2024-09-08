'''
Implement Min stack
list(tuple/set)

[actuaValue, curMin]  <--> same can be done for Max Stack
[1,0]
[0,1]
[3,2]
'''

class MinMaxStack:
    def __init__(self):
        self.st = []

    def push(self, x):
        # Get Min 
        curMin = self.getMin()

        # Get Max
        curMax = self.getMax()

        # None for base case 
        # Current Min
        if(curMin == None or curMin > x):
            curMin = x
        self.st.append((x,curMin, curMax))
        
        # Append Current Max
        if(curMax == None or curMax < x):
            curMax = x
        self.st.append((x, curMin, curMax))
        
    def pop(self):
        return self.st.pop() if self.st else None 

    def top(self):
        #actual value in the stack
        return self.st[-1][0]

    def getMax(self):
        if(self.st):
            #return max value (Actualvalue, MinValue, MaxValue)
            return self.st[-1][2]
        return None

    def getMin(self):
        #return min value in the stack : always on the top
        if(self.st):
            return self.st[-1][1]
        return None
       # return self.st[-1][1] if self.st else None         # One liner


if __name__ == "__main__":
    ms = MinMaxStack()
    ms.push(4)
    ms.push(5)
    ms.push(1)
    ms.push(2)
    
    
    print(ms.top())
    print(ms.getMax())
    print(ms.getMin())


    '''
    2, 1
    3, 1
    1, 1

    ans::
    stack - 1 
    curMin - 0
    '''