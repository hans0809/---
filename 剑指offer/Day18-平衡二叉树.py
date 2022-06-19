# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
# 如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_height(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            return 1+max(get_height(root.left),get_height(root.right))
        def dfs(root):
            if not root:
                return True
            if not root.left and not root.right:
                return True
            left_height=get_height(root.left)
            right_height=get_height(root.right)
            if abs(left_height-right_height)>1:
                return False
            return dfs(root.left) and dfs(root.right)
        
        return dfs(root)