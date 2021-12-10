'''
TC  : O(V+E)
SC : O(V)
- We can implement BFS using queue.
'''

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def BFS(self, startNode):
        visited = set()
        queue = []
        queue.append(startNode)

        #first ele is visited
        visited.add(startNode)

        while(queue):
            cur = queue.pop(0)
            print(cur, end=" ")

            for v in self.graph[cur]:
                if(v not in visited):
                    queue.append(v)
                    visited.add(v)


g = Graph()
g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(6,9)

g.BFS(2)   # 2 > 1 > 5 > 6 > 8 > 9 
        