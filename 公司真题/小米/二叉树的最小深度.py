# 给定一个二叉树，找出其最小深度。

# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:#是叶子结点
            return 1

        if root.left:
            left=self.minDepth(root.left)#左子树最小深度
        if root.right:
            right=self.minDepth(root.right)#右子树最小深度
        if root.left and root.right:
            return 1+min(left,right)
        if root.left:
            return 1+left
        if root.right:
            return 1+right     
