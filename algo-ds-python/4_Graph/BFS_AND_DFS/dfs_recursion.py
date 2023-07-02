'''
DFS usign Recursion.
TC  : O(V+E)
SC : O(V)

'''

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
        
    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Using Recursion 
    def DFS(self, array):
        array.append(self.name)
        for child in self.children:
            child.DFS(array)
        return array


g = Node(2)

g.addChild(1)
g.addChild(5)

#adding children
g.children[1].addChild(6)
g.children[1].addChild(8)

g.children[1].children[0].addChild(9)


dfs = g.DFS([])  
print(dfs)   # Result : [2, 1, 5, 6, 9, 8]