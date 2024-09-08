class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_distinct_paths(root, cur_path=[]):
    """
    Prints all distinct paths from root to leaf in a tree.

    Args:
        root: The root node of the tree.
        cur_path: The current path (list of node values) being explored.
        seen: A set to keep track of visited nodes (prevents duplicates).
    """
    if not root:
        return

    cur_path.append(root.val)

    if not root.left and not root.right:
        # Leaf node, print the path
        print(cur_path)  # Print a copy to avoid modifications

    # Explore left subtree if it exists and hasn't been visited fully
    print_distinct_paths(root.left, cur_path)

    # Explore right subtree if it exists and hasn't been visited fully
    print_distinct_paths(root.right, cur_path)

    # Backtrack, remove current node from path
    cur_path.pop()

    

        
if __name__ == '__main__':
    root = Node(4)
    root.left = Node(0)
    root.right = Node(1)

    root.right.left = Node(3)
    root.right.left.right = Node(5)

    root.right.right = Node(2)


    print(print_distinct_paths(root))

