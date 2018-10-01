# Binary Search Tree
import unittest
class Node(object):
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def __lt__(self, val):
        return self.val < val

    def __gt__(self, val):
        return self.val > val

    def __eq__(self, val):
        return self.val == val
    # Insert fun is recursive, digs into tree until correct place to insert data is found


# Tree class will be the main user interface
class Tree:
    # Define constructor
    def __init__(self):
        self.root = None
    # Accepts a piece of data to insert
    # Returns true if data does not currently exist
    def insert(self, data):
        # Checks if root node exists, if yes call recursive insert function
        if self.root:
            return self.insert(self.root, data)

        # If does not exist, create new node and return false
    def _insert(self, node, data):
        if node is None:
            node = Node(data)
        if data > node:
            node.leftChild = self._insert(node.leftChild, data)
        elif data > node:
            node.rightChild = self._insert(node.rightChild, data)
        else:
            node.data = data
            return node
    def find(self, data):
        return self.find(self.root, data)

    def _find(self, node, data):
        while not node is None:
            if data < node: node = node.leftChild
            elif data > node: node = node.rightChild
            else: return node.data

        return None


        # This method returns `None` if no common is found
    def find_common(self, a, b):
        return self._find_common(self.root, a, b)

    def _find_common(self, node, a, b):
        if node is None:
            return None
        # Traverse right until a diverge occurs
        if a > node and b > node:
            if node.right is None: return None

            # if right node is `a` or `b` then we have found common
            if node.right == a or node.right == b:
                return node.val

            return self._find_common(node.right, a, b)

        # Traverse left until a diverge occurs
        elif a < node and b < node:
            if node.left is None: return None

            # if left node is `a` or `b` then we have found common
            if node.left == a or node.left == b:
                return node.val

            return self._find_common(node.left, a, b)

        # root does not have any common ancestor
        # This test is later because we dont want the
        # recursion to hit it every time
        elif a == self.root or b == self.root:
            return None

        else:
            # A diverge of the tree traversal occurs here
            # So the current node is a potential common ancestor
            # Verify that a and b are legitimate nodes
            if self._node_exists(node, a):
                # `a` exists ensure `b` exists
                if self._node_exists(node, b):
                    # Common ancestor is validated
                    return node.val
                else:
                    return None
            else:
                return None

    def _node_exists(self, node, val):
        return not self._find(node, val) is None

class TestMethods(unittest.TestCase):

    def testConstructor(self):
        BinarySearchTree =Tree()
        self.assertEqual(BinarySearchTree.root, None)

    def testEmptyTree(self):
        BinarySearchTree=Tree()
        self.assertEqual(BinarySearchTree.find_common(1, 2), None)


BinarySearchTree = Tree()
print(BinarySearchTree.insert(10))
print(BinarySearchTree.insert(10))
print(BinarySearchTree.find_common('a', 'b'))
BinarySearchTree.insert(14)
BinarySearchTree.insert(7)
unittest.main(exit=False)

