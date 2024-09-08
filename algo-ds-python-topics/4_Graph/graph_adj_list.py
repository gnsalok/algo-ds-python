'''
Graph Implementation : Adjacency List
'''
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def printGraph(self):
        for node in self.graph: # getting nodes <key in dict>
            for v in self.graph[node]: # getting values at node <list values at per key>
                print(node, "=>", v)




if __name__ == "__main__":
    g = Graph()
    g.insertEdge(1,5)
    g.insertEdge(5,2)
    g.insertEdge(2,7)
    g.insertEdge(7,1)

    g.printGraph()
    

