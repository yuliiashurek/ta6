import random
import time
import numpy as np


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def __reassign_nodes(self, node, new_children):
        if new_children is not None:  # reset its kids
            new_children.parent = node.parent
        if node.parent is not None:  # reset its parent
            if self.is_right(node):  # If it is the right children
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def is_right(self, node):
        return node == node.parent.right

    def empty(self):
        return self.root is None

    def insert(self, value):

        new_node = Node(value, None)  # create a new Node
        if self.empty():  # if Tree is empty
            self.root = new_node  # set its root
        else:  # Tree is not empty
            parent_node = self.root  # from root
            while True:  # While we don't get to a leaf
                if value < parent_node.value:  # We go left
                    if parent_node.left is None:
                        parent_node.left = new_node  # We insert the new node in a leaf
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def search(self, value):
        if self.empty():
            raise IndexError("Warning: Tree is empty! please use another.")
        else:
            node = self.root
            # use lazy evaluation here to avoid NoneType Attribute error
            while node is not None and node.value is not value:
                node = node.left if value < node.value else node.right
            return node

    def get_max(self, node=None):
        if node is None:
            node = self.root
        if not self.empty():
            while node.right is not None:
                node = node.right
        return node

    # def get_min(self, node=None):
    #     """
    #     We go deep on the left branch
    #     """
    #     if node is None:
    #         node = self.root
    #     if not self.empty():
    #         node = self.root
    #         while node.left is not None:
    #             node = node.left
    #     return node

    def remove(self, value):
        node = self.search(value)  # Look for the node with that label
        if node is not None:
            if node.left is None and node.right is None:  # If it has no children
                self.__reassign_nodes(node, None)
            elif node.left is None:  # Has only right children
                self.__reassign_nodes(node, node.right)
            elif node.right is None:  # Has only left children
                self.__reassign_nodes(node, node.left)
            else:
                tmp_node = self.get_max(
                    node.left
                )  # Gets the max value of the left branch
                self.remove(tmp_node.value)
                node.value = (
                    tmp_node.value
                )  # Assigns the value to the node to delete and keep tree structure


def make_random_array(num):
    a = []
    for i in range(num):
        a.append(random.randint(1, 100000))
    return a


if __name__ == '__main__':
    t = BinarySearchTree()
    # lst = make_random_array(1000)
    # start = time.time()
    # for x in lst:
    #     t.insert(x)
    # end = time.time()
    # print("Insertion in BST tree, random: ", end - start)

    start = time.time()
    list2 = np.arange(1, 1000, 1)
    for x in list2:
        t.insert(x)
    end = time.time()
    print("Insertion in RB tree, not random: ", end - start)

    # start3 = time.time()
    # for x in range(1, 1000):
    #     t.search(99)
    # end3 = time.time()
    # print("Searching in BST tree: ", end3 - start3)
    #
    # start2 = time.time()
    # for x in range(1, 1000):
    #     t.remove(x)
    # end2 = time.time()
    # print("Deletion in BST tree: ", end2 - start2)
