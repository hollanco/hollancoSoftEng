#Binary Search Tree


class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
    #Insert fun is recursive, digs into tree until correct place to insert data is found
    def insert(self, data):
        #Prevent creation of duplicates
        if self.value == data:
            return False
        #Less than current node, look to the left
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        #Greater than current node, look to the right
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
    #Recursively checks through tree to find if data passed is present
    def find(self, data):
        if (self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()
#Tree class will be the main user interface
class Tree:
    #Define constructor
    def __init__(self):
        self.root = None
    #Accepts a piece of data to insert
    #Returns true if data does not currently exist
    def insert(self, data):
        #Checks if root node exists, if yes call recursive insert function
        if self.root:
            return self.root.insert(data)
        #If does not exist, create new node and return false
        else:
            self.root = Node(data)
            return True
    #Calls find on root node if root exists
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    def inorder(self):
        print("InOrder")
        self.root.inorder()

BinarySearchTree = Tree()
print(BinarySearchTree.insert(10))
print(BinarySearchTree.insert(10))
BinarySearchTree.insert(14)
BinarySearchTree.insert(7)
BinarySearchTree.preorder()
BinarySearchTree.inorder()