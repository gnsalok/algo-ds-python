class Node:
    def __init__(self, name):
        self.children = []  # edges, or the childrens
        self.name = name  # name of the node 

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]  # root node
        while(queue):
            cur = queue.pop(0)
            array.append(cur.name)
            for child in cur.children:
                queue.append(child)
        return array


if __name__ == "__main__":
    graph = Node("A")  # root node
    graph.addChild("B")
    graph.addChild("C")

    graph.children[0].addChild("F")
    graph.children[0].addChild("G")

    #TODO graph.printGraph()
 
    bfsResut = graph.breadthFirstSearch([])
    print("BFS Array", bfsResut)
