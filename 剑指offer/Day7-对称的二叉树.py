# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(root1,root2):
            # 全为空
            if not root1 and not root2:
                return True
            # 只有一个为空
            if (not root1 and root2) or(root1 and not root2):
                return False
            # 都不为空但根节点值不同
            if root1.val !=root2.val:
                return False
            # 检查左右子树是否对称
            return check(root1.left,root2.right) and check(root1.right,root2.left)
        return check(root,root)
        