# 给定二叉树的根节点 root ，返回所有左叶子之和。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res=0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def run(root):
            if not root:
                return 0
            # if not root.left and not root.right:
            #     return 0# 加不加都可以
            if root.left and not root.left.left and not root.left.right:
                self.res+=root.left.val
            
            run(root.left)
            run(root.right)
            
        run(root)
        return self.res