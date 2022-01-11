'''
Graph Implementation : Adjacency List Undirected Graph 
'''
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1) #adding this link will make this program undirected graph 

    def printGraph(self):
        for node in self.graph: # getting nodes >> {1: [5, 7], 5: [1, 2], 2: [5, 7], 7: [2, 1]})
            for v in self.graph[node]: #getting values at node
                print(node, "=>", v)

if __name__ == "__main__":
    g = Graph()
    g.insertEdge(1,5)
    g.insertEdge(5,2)
    g.insertEdge(2,7)
    g.insertEdge(7,1)

    g.printGraph()
    

