'''
BFS Implementation using Queue using core Data Structure.
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

    def BFS(self,startNode, array):
        queue = []
        queue.append(startNode)
        while(queue):
            cur = queue.pop(0)
            array.append(cur.name)
            for child in cur.children:
                queue.append(child)
        return array


g = Node(2)

g.addChild(1)
g.addChild(5)

#adding children
g.children[0].addChild(6)
g.children[0].addChild(8)
g.children[1].addChild(9)


bfs = g.BFS(g, [])  
print(bfs)