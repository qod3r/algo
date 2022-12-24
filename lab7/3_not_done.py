from ppbtree import *


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
    
class Node:
    def __init__(self, val, is_question=True):
        self.val = val
        self.is_question = is_question
    
    def __repr__(self):
        return self.val


if __name__ == "__main__":
    # t = BinaryTree(Node('Это млекопитающее?'))
    t = BinaryTree(Node('Оно лает?'))
    t.insertRight(Node('Собака', False))
    t.insertLeft(Node('Кошка', False))
    
    t1 = BinaryTree(Node('Это млекопитающее?'))
    t1.insertLeft(t)
    
    
    print_tree(t1, nameattr='key', left_child='leftChild', right_child='rightChild')