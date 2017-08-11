# 3.6.1
# -*- coding:UTF-8 -*-

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TraversalBinaryTree:
    def preOrder(self, tree):
        if tree == None:
            return
        print(tree.data)
        self.preOrder(tree.left)
        self.preOrder(tree.right)

    def midOrder(self, tree):
        if tree == None:
            return
        self.midOrder(tree.left)
        print(tree.data)
        self.midOrder(tree.right)

    def postOrder(self, tree):
        if tree == None:
            return
        self.midOrder(tree.left)
        self.midOrder(tree.right)
        print(tree.data)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

TraversalBinaryTree().preOrder(root)
print("===============")
TraversalBinaryTree().midOrder(root)
print("===============")
TraversalBinaryTree().postOrder(root)
