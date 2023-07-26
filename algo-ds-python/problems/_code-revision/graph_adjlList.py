'''
Graph representation by adjacency list 
'''

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)  # {5:[1,2,3]}
        # self.graph[v2].append(v1) This will make this undirected graph

    def printGraph(self):
        for node in self.graph:
            print(self.graph[node])
            for v in self.graph[node]:
                print(f"{node} => {v}")

def main():
    g = Graph()
    g.insertEdge(1, 5)
    g.insertEdge(5, 2)
    g.insertEdge(2, 7)
    g.insertEdge(7, 1)

    g.printGraph()


if __name__ == "__main__":
    main()
