'''
BFS Implementation using Queue and python defaultdict.
TC  : O(V+E)
SC : O(V)
'''

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def BFS(self, startNode):
        q = []
        q.append(startNode)

        while(q):
            cur = q.pop(0)
            print(cur, end=" ")

            for vertex in self.graph[cur]:
                q.append(vertex)



g = Graph()
g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(6,9)

g.BFS(2)  # 2 > 1 > 5 > 6 > 8 > 9 

