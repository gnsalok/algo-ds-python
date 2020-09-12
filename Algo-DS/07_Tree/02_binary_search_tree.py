"""
Author: Santosh Pillai
Email: santosh.pillai98@gmail.com
"""


class Node:
    """ Node Class """
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        """
        Insert node in the Tree recursively.
        :param data:
        :return:
        """
        # avoid duplicate values:
        if self.data is data:
            return False
        elif self.data > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            print('insert {} in right.'.format(data))
            if self.right:
                return self.right.insert(data)
            else:
                self.right  = Node(data)
                return True

    def find(self, data):
        """
        Find a data in the tree
        :param data:
        :return:
        """
        if self.data is data:
            return True
        elif self.data > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        """
        Preorder traversal of the node
        :return:
        """
        if self:
            print(str(self.data))
            if self.left:
                return self.left.preorder()
            if self.right:
                return self.right.preorder()

    def postorder(self):
        """
        post order traversal - left right root
        :return:
        """
        if self:
            if self.left:
                return self.left.postoder()
            if self.right:
                return self.right.postorder()


    def height(self):
        """ 
        Get height of the tree
        """
        if self.right and self.left:
            print(self.data)
            return 1 + max(self.left.height(), self.right.height())
        elif self.right:
            print(self.data)
            return 1 + self.right.height()
        elif self.left:
            print(self.data)
            return 1 + self.left.height()
        else:
            print(self.data)
            return 1   # only has root node.


    def BFS(self, level):
        """ Level Order Traversal """
        if level == 1:
            print(self.data)
        elif level > 1:
            if self.left:
                self.left.BFS(level-1)
            if self.right:
                self.right.BFS(level-1)

                                             


class BST:
    """ Binary Search Tree """
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert a new node to the tree
        :param data:
        :return:
        """
        if self.root is None: # Tree is empty.
            self.root = Node(data)
            return True
        else:
            return self.root.insert(data)

    def find(self, data):
        """ Find a data in the tree """
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        """
        Pre-order traversal of the node
        :return:
        """
        print(' --- Pre order ---- ')
        self.root.preorder()

    def inorder(self, root):
        """
        Inorder travesal of the tree
        :return:
        """
        if root:
            if root.left:
                return self.inorder(root.left)
            print(str(root.data))
            if root.right:
                return self.inorder(root.right)

    def postorder(self):
        """
        Post Order traversal
        :return:
        """
        print(' ---- Post Order traveral ')
        self.root.postorder()

    def size(self, root):
        """
        size of the BST
        :return:
        """
        if root is not None:
           return self.size(root.left) + 1 + self.size(root.right)
        else:
            return 0

    def height(self):
        """ Get Height """
        if self.root:
            return self.root.height()
        else:
            return 0

    def BFS(self):
        if self.root is None:
            return False
        else:
            for level in range(1, self.height()+1):
                self.root.BFS(level)

if __name__ == '__main__':
    bst = BST()
    print(bst)
    print(bst.insert(10))
    print(bst.insert(8))
    print(bst.insert(9))
    print(bst.insert(4))
    print(bst.insert(5))
    print(bst.insert(22))
    print(bst.insert(6))
    print(bst.find(12))
    #print(bst.size())
    print(bst.inorder(bst.root))
    print('here')
    print("height of tree -- " + str(bst.height()))
    print("Level Order Traversal")
    bst.BFS()
    print("Depth first Search")
    print("--- Preorder ---")
    bst.preorder()
