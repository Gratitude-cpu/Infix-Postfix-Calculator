# Program: Calculator 
# author: Manusri Allam
# date: 3/6/2023
'''
# file: Calculator is a program that takes an expression from the user, then does infix to postfix conversion,
makes a tree using stack functionality to organize the various operators and operands. Finally does the calculation
and returns the final answer to the expression. The programn gets advanced by implementing a GUI (a global user interface)
'''
# input: Inputs that are given by the user is the expression to evaluate by the calculator program
# output: It outputs an answer as a float to the given expression provided by the user.
from stack import Stack
#This is the class Binary Tree
class BinaryTree:
    #Initializes the rootobj, leftchild, and rightchild to none
    def __init__(self, rootObj=None):
        self.rootObj = rootObj
        self.leftChild = None
        self.rightChild = None
    #The way it inserts the to the left of the binary tree
    def insertLeft(self, newNodeVal):
            t = BinaryTree(newNodeVal)
            t.leftChild = self.leftChild
            self.leftChild = BinaryTree(newNodeVal)
    #The way it inserts to the right side of the tree
    def insertRight(self, newNodeVal):
            t = BinaryTree(newNodeVal)
            t.rightChild = self.rightChild
            self.rightChild = BinaryTree(newNodeVal)
    #Returns the rightchild
    def getRightChild(self):
        return self.rightChild
    #returns the leftchild
    def getLeftChild(self):
        return self.leftChild
    #returns the rootobj
    def getRootVal(self):
        return self.rootObj
    #this sets the rootVal
    def setRootVal(self, obj):
        self.rootObj = obj
        return self.rootObj
    #Formats everything into a string format as well as adding parenthesis
    def __str__(self):
        s = f"{self.rootObj}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s
#This is class Expression Tree
class ExpTree(BinaryTree):
    #Here we are making the tree using various stack functionalities.
    def make_tree(postfix):
        #pop and return final stack value s = Stack()
        s = Stack()
        for op in postfix: 
            if op.isalnum():
                s.push(ExpTree(op))
            else:
                rights = s.pop() 
                lefts = s.pop()
                tree = ExpTree (op)
                tree.rightChild = rights
                tree.leftChild = lefts
                s.push(tree)
        return s.pop()

    #This is preordering the expression so basically getting it right from the tree
    def preorder(tree):
        s = ''
        if tree is not None:
            s += tree.getRootVal()
            s += ExpTree.preorder(tree.leftChild)
            s += ExpTree.preorder(tree.rightChild)
        return s

    #Putting all the operands and operators from preorder 
    def inorder(tree):
        s = ''
        if tree.getLeftChild() is not None:
            s += '('
            s += ExpTree.inorder(tree.getLeftChild())
        s += tree.getRootVal()
        if tree.getRightChild() is not None:
            s += ExpTree.inorder(tree.getRightChild())
            s += ')'
        return s
            
    #Putting all the operands and operators from the inorder so getting everything ready for evaluation
    def postorder(tree):
        s = ''
        if tree is not None:
            s += ExpTree.postorder(tree.leftChild)
            s += ExpTree.postorder(tree.rightChild)
            s += tree.getRootVal()
        return s
   #Finally uses the postfix format to evaluation the expression to one floating point value
    def evaluate(tree):
        if tree.getLeftChild() and tree.getRightChild():
            rootrootObj = tree.getRootVal()

            left_val = ExpTree.evaluate(tree.getLeftChild())
            right_val = ExpTree.evaluate(tree.getRightChild())

            if rootrootObj == '+':
                return left_val + right_val
            elif rootrootObj == '-':
                return left_val - right_val
            elif rootrootObj == '*':
                return left_val * right_val
            elif rootrootObj == '^':
                return left_val ** right_val
            else:
                return left_val / right_val
        else:
            return float(tree.getRootVal())
    #This is the string format from the inorder expression
    def __str__(self):
        return ExpTree.inorder(self)
     
'''
This is the driver code to test the methods of the binary tree and expression tree
'''
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'
    
    # test an ExpTree
    
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    #print(str(tree))
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0
    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0

    
    