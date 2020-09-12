"""
Author: Santosh Pillai
Email: santosh.pillai98@gmail.com
"""


class Node:
    """ Node Class """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class SimpleTree:
    """ Binary Search Tree """
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert data into the Simple Tree
        :param data:
        :return:
        """

        # if empty
        if self.root is None:
            self.root = Node(data)
            return True

        cur_node = self.root
        while True:
            if cur_node.left is not None:
                cur_node



if __name__ == '__main__':
    tree = SimpleTree
    print(tree)