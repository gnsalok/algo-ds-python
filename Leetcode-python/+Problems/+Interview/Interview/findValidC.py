from typing import List

def findValidC(cp : List[int]) -> int:
    list = []
    
    for c in cp:
        stack = []
        for i in range(0, len(c)):
            if(not len(stack)==0 and stack[len(stack)-1] == c[i]):
                stack.pop()
            else:
                stack.append(c[i])
        
        if(len(stack) == 0):
            list.append(1)
        else:
            list.append(0)
    return list 


if __name__ == "__main__":
    arr = ["abba", "abca", "abbacbbc", "aabb", "xaaxybbyzccz", "vaas", "jay"]
    result = findValidC(arr)
    print(result)
        
                
            





