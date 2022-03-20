
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
        
    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def DFS(self, startNode, array):
        st = []
        st.append(startNode)
        while(st):
            cur = st[-1]
            st.pop()
            array.append(cur.name)
            for child in cur.children:
                st.append(child)
        return array


g = Node(2)

g.addChild(1)
g.addChild(5)

#adding children
g.children[1].addChild(6)
g.children[1].addChild(8)

g.children[1].children[0].addChild(9)


dfs = g.DFS(g, [])  
print(dfs)