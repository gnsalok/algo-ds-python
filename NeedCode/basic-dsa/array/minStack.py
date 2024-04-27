'''
MinStack 
https://leetcode.com/problems/min-stack/

'''

class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        curMin = self.getMin()
        if curMin == None or val < curMin:
            curMin = val
        self.st.append((val, curMin))
        

    def pop(self) -> None:
        self.st.pop()
        
    def top(self) -> int:
        return self.st[-1][0]


    def getMin(self) -> int:
        if self.st:
            return self.st[-1][1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
