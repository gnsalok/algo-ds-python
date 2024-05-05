'''
delete a node in BST

https://leetcode.com/problems/delete-node-in-a-bst/

''' 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min = self.getMinValue(root.right)
                # replace min with BST root
                root.val = min
                # remove the min value from BST as it's already replaced with root
                root.right = self.deleteNode(root.right, root.val)
        return root


    # get the minimum from right subtree
    def getMinValue(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr.val