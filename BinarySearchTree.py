# Binary Search Tree
import unittest


class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def __lt__(self, data):
        return self.data < data

    def __gt__(self, data):
        return self.data > data

    def __eq__(self, data):
        return self.data == data

    def __str__(self):
        return "[Node data: %d]" % self.data

    # Insert fun is recursive, digs into tree until correct place to insert data is found


# Tree class will be the main user interface
class Tree(object):
    # Define constructor
    def __init__(self):
        self.root = None

    # Accepts a piece of data to insert
    # Returns true if data does not currently exist
    def insert(self, data):
        # Checks if root node exists, if yes call recursive insert function
        self.root = self._insert(self.root, data)

        # If does not exist, create new node and return false
    def _insert(self, node, data):
        if node is None:
            node = Node(data)
        if data < node:
            node.leftChild = self._insert(node.leftChild, data)
        elif data > node:
            node.rightChild = self._insert(node.rightChild, data)
        else:
            node.data = data

        return node

    def find(self, data):
        return self._find(self.root, data)

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
                return node.data

            return self._find_common(node.right, a, b)

        # Traverse left until a diverge occurs
        elif a < node and b < node:
            if node.leftChild is None: return None

            # if left node is `a` or `b` then we have found common
            if node.leftChild == a or node.leftChild == b:
                return node.data

            return self._find_common(node.leftChild, a, b)

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
                    return node.data
                else:
                    return None
            else:
                return None

    def node_exists(self, data):
        return self._node_exists(self, data)

    def _node_exists(self, node, data):
        return not self._find(node, data) is None


class TestMethods(unittest.TestCase):

    def testConstructor(self):
        bst1 = Tree()
        self.assertEqual(bst1.root, None)

    def testEmptyTree(self):
        bst2 = Tree()
        self.assertEqual(bst2.find_common(1, 2), None)

    def test_non_empty_tree(self):
        bst3 = Tree()
        bst3.insert(10)
        self.assertEqual(bst3.find(10), 10)

    def test_left_child(self):
        bst = Tree()
        bst.insert(10)
        bst.insert(7)
        self.assertEqual(bst.find(7), 7)

    def test_right_child(self):
        bst2 = Tree()
        bst2.insert(10)
        bst2.insert(13)
        self.assertEqual(bst2.find(13), 13)

    def test_double_insert(self):
        bst3 = Tree()
        bst3.insert(10)
        bst3.insert(10)
        self.assertEqual(bst3.find(10), 10)

    def test__find_common(self):
        bst = Tree()
        bst.insert(20)
        bst.insert(8)
        bst.insert(22)
        bst.insert(4)
        bst.insert(12)
        bst.insert(10)
        bst.insert(3)
        self.assertEqual(bst.find_common(3, 10), 8)
        self.assertEqual(bst.find_common(3, 22), 20)
        self.assertEqual(bst.find_common(4, 10), 8)
        self.assertEqual(bst.find_common(8, 22), 20)


bstree = Tree()
print(bstree.insert(10))
print(bstree.insert(10))
bstree.insert(14)
bstree.insert(7)
unittest.main(exit=False)

