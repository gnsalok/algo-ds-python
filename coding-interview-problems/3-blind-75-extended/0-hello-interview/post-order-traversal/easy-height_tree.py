'''
Calculate the height of a binary tree.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def height(root: TreeNode) -> int:
    '''
    Calculate the height of a binary tree.
    
    Args:
    root: TreeNode, the root of the binary tree.
    
    Returns:
    int, the height of the binary tree.
    '''
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Calculate the height of the binary tree
    print("Height of the binary tree:", height(root))  # Output: 3