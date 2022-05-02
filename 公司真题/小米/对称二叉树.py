# 给你一个二叉树的根节点 root ， 检查它是否轴对称。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def do(r1,r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            if r1.val !=r2.val:
                return False
            return do(r1.left,r2.right) and do(r1.right,r2.left)

        if not root:
            return True
        if not root.left and not root.right:
            return True
        
        return do(root.left,root.right)