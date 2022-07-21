# 给定一个二叉树，判断它是否是高度平衡的二叉树。

# 本题中，一棵高度平衡二叉树定义为：

# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(root):
            if not root:
                return 0
            return 1+max(getHeight(root.left),getHeight(root.right))
        
        def run(root):
            if not root:
                return True
            left_height=getHeight(root.left)
            right_height=getHeight(root.right)
            if abs(left_height-right_height)>1:
                return False
            return run(root.left) and run(root.right)
        
        return run(root)