class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None


class Tree:
    "Binary Search Tree"
    def __init__(self):
        self.root = None 

    def insert(self, data):
        # if empty
        if self.root is None:
            self.root = Node(data)
        
        cur_node = self.root 
        while True:
            if cur_node.left is not None:
                cur_node

    


if __name__ == "__main__":
    tree = Tree()
    print(tree)

    tree.insert(11)
    tree.insert(12)
    tree.insert(13)

    print(tree)


         

        