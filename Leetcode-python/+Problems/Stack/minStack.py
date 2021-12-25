'''
Implement Min stack
list(tuple/set)

[actuaValue, curMin]  <--> same can be done for Max Stack
[1,0]
[0,1]
[3,2]
'''

class MinStack:
    def __init__(self):
        self.st = []

    def push(self, x):
        curMin = self.getMin()
        #None is for first case 
        if(curMin == None or curMin > x):
            curMin = x
        self.st.append((x,curMin))

    def pop(self):
        return self.st.pop() if self.st else None 

    def top(self):
        #actual value in the stack
        return self.st[-1][0]

    def getMin(self):
        #return min value in the stack : always on the top
        if(self.st):
            return self.st[-1][1]
        return None
       # return self.st[-1][1] if self.st else None         # One liner


if __name__ == "__main__":
    ms = MinStack()
    ms.push(1)
    ms.push(3)
    ms.push(2)
    
    print(ms.top())