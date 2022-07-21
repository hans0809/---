# 给你一个二叉树的根节点 root ， 检查它是否轴对称。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def run(left,right):
            if left and not right:
                return False
            elif not left and right:
                return False
            elif not left and not right:
                return True
            elif left.val!=right.val:
                return False
            else:
                return run(left.left,right.right) and run(left.right,right.left)

        return run(root.left,root.right)