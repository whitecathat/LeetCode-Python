# 3.6.1
# -*- coding:UTF-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MaxDepthOfBinaryTree:
    def solve(self, root):
        if root is None:
            return 0
        else:    
            return min(self.solve(root.left), self.solve(root.right)) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print(MaxDepthOfBinaryTree().solve(root))