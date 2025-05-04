'''
Problem : Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    max_diameter = 0
    '''
    Calculate the diameter of a binary tree.

    Args:
    root: TreeNode, the root of the binary tree.

    Returns:
    int, the diameter of the binary tree.
    '''
    def dfs(node):
        nonlocal max_diameter
        if not node:
            return 0
            
        left_height = dfs(node.left)
        right_height = dfs(node.right)


        max_diameter = max(max_diameter, left_height + right_height)
        return 1 + max(left_height, right_height)

    
    dfs(root)
    return max_diameter

# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Calculate the diameter of the binary tree
    print("Diameter of the binary tree:", diameterOfBinaryTree(root))  # Output: 3

