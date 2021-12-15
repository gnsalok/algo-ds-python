'''
Graph Implementation using Adjacency Matrix.
'''


class Graph:
    def __init__(self, noOfNodes):
        self.noOfNode = noOfNodes + 1

        self.graph = [[0 for x in range(noOfNodes+1)]
                       for y in range(noOfNodes+1)]

    def withInBounds(self, v1, v2):
        return (v1 >= 0 and v1 <= self.noOfNode) and (v2 >= 0 and v2 <= self.noOfNode)

    
    def insertEdge(self, v1, v2):
        if(self.withInBounds(v1,v2)):
            self.graph[v1][v2] = 1
            self.graph[v2][v1] = 1

    def printGraph(self):
        print(self.graph)
        for i in range(self.noOfNode):
            for j in range(len(self.graph[i])):
                if(self.graph[i][j]):
                    print(i, "-->",j)





g = Graph(5)
g.insertEdge(1,2)
g.insertEdge(2,3)
g.insertEdge(3,4)

g.printGraph()


    

        

        