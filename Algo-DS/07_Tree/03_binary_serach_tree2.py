"""
Author: Santosh Pillai
Email: santosh.pillai98@gmail.com
"""


class Node:
    """ Node Implementation"""
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        """
        Inserting new data into the BST
        :param data:
        :return:
        """
        if self.data is data:
            print('{} is already present in the Tree'.format(data))
            return False

        if data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        """
        Find data in a BST
        :param data:
        :return:
        """
        if self.data is data:
            return True

        if self.data > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def in_order(self):
        """
        In order tree traversal
        :param resp:
        :return:
        """
        if self:
            if self.left:
                return self.left.in_order()
            print('here1')
            print(str(self.data))
            if self.right:
                print('here2')
                return self.right.in_order()

class BST2:
    """ Binary Search Tree implementation """
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert new data in the BST
        :param data:
        :return:
        """
        print(' --- Adding {} to the BST ---'.format(data))
        # if Tree is empty:
        if self.root is None:
            self.root = Node(data)
            return True
        else:
            self.root.insert(data)
            return True

    def find(self, data):
        """
        Find data in the BST
        :param data:
        :return:
        """
        print(' ---Finding {} in the BST'.format(data))
        # if tree is empty
        if self.root is None:
            return False
        else:
            return self.root.find(data)

    def in_order(self, node, resp):
        """
        BST Preprder traversal
        :return:
        """
        if node is not None:
            self.in_order(node.left, resp)
            resp.append(node.data)
            self.in_order(node.right, resp)
        return resp

    def pre_order(self, node, resp):
        if node is not None:
            resp.append(node.data)
            self.pre_order(node.left, resp)
            self.pre_order(node.right, resp)
        return resp

    def post_order(self, node, resp):
        if node is not None:
            self.post_order(node.left, resp)
            self.post_order(node.right, resp)
            resp.append(node.data)
        return resp


if __name__ == '__main__':
    bst = BST2()
    print(bst.insert(5))
    print(bst.insert(1))
    print(bst.insert(10))
    print(bst.insert(20))
    print(bst.insert(8))
    print(bst.insert(4))
    print(bst.insert(2))
    # print(bst.root.data)
    # print(bst.root.left.data)
    # print(bst.root.right.data)
    print(bst.find(11))
    print(bst.in_order(bst.root, []))
    print(bst.pre_order(bst.root, []))
    print(bst.post_order(bst.root, []))