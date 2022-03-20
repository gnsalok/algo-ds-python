'''
DFS using stack and python defaultdict.
TC  : O(V+E)
SC : O(V)  [Vertex / Node]
'''

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def DFS(self, startNode):     
        st = []
        st.append(startNode)

        while(st):
            cur = st[-1]
            st.pop()   
            print(cur, end=" ")
            
            for vertex in self.graph[cur]:
                st.append(vertex)
                #print("cur stack->",vertex)
                    


g = Graph()
g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(6,9)

g.DFS(2)  # 2 > 5 > 8 > 6 > 9 > 1


