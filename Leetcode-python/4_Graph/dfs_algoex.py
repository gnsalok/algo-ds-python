class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name) #appeding nodes on each traversal recursively 
        for child in self.children:
            child.depthFirstSearch(array)
        return array


if __name__ == "__main__":
    graph = Node("A")  # root node
    graph.addChild("B")
    graph.addChild("C")

    graph.children[0].addChild("F")
    graph.children[0].addChild("G")

    # TODO graph.printGraph()

    dfsResut = graph.depthFirstSearch([])
    print("DFS Array", dfsResut)  # A B F G C
