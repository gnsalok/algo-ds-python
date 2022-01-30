class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
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

    bfsResut = graph.depthFirstSearch([])
    print("DFS Array", bfsResut)  # A B F G C
