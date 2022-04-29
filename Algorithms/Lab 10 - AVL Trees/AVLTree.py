from bridges.avl_tree_element import *


class AVLTree():
    def __init__(self, filename):
        self.nodes = []

        # read keys from txt file
        File = open(filename)
        for key in File:
            # create an AVL tree elements
            self.nodes.append(AVLTreeElement(int(key), key))
        File.close()
        # initialize the root as empty
        self.root = None
        # build the tree
        self.build()

    # build the tree
    def build(self):
        # insert node to the tree one by one
        for node in self.nodes:
            self.root = self.insert(node, self.root)

    # insert one node to current tree
    def insert(self, node, root):
        if not root:
            root = node
        # go to the left
        elif node.key < root.key:
            root.left = self.insert(node, root.left)
        # go to the right
        else:
            root.right = self.insert(node, root.right)

        # Call self.height to calculate balance factor for the root of current subtree
        # You should set the balance factor using something like:
        #           root.balance_factor = the value of balance factor

        # Balance current subtree if root.balance_factor is greater than 1 or less than -1
        # You can use these library functions:
        #           node.key
        #           node.left
        #           node.right
        # For more library functions, please go to:
        #     http://bridgesuncc.github.io/doc/python-api/current/html/classbridges_1_1avl__tree__element_1_1_a_v_l_tree_element.html

        # your code goes here:
        root.balance_factor = self.height(root.left) - self.height(root.right)
        if root.balance_factor > 1:
            if node.key < root.left.key:
                root = self.right_rotation(root)
            else:
                root.left = self.left_rotation(root.left)
                root = self.right_rotation(root)
        elif root.balance_factor < -1:
            if node.key > root.right.key:
                root = self.left_rotation(root)
            else:
                root.right = self.right_rotation(root.right)
                root = self.left_rotation(root)
        # recursively return root of current subtree
        return root


    # rotate to the left
    def left_rotation(self, root):
        # your code goes here:
        temp = root
        root = root.right
        if root.left is not None:
            node = root.left
            temp.right = node
        else:
            temp.right = None
        root.left = temp

        return root

    # rotate to the right
    def right_rotation(self, root):

        # your code goes here:
        temp = root
        root = root.left

        if root.right is not None:
            node = root.right
            temp.left = node
        else:
            temp.left = None
        root.right = temp

        return root

    def height(self, node):
        if not node:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

    def root(self):
        return self.root