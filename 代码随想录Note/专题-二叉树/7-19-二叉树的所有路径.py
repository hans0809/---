# 给定一个二叉树，返回所有从根节点到叶子节点的路径。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        path=[]
        res=[]
        def backtrack(root):
            path.append(root.val)
            if not root.left and not root.right:
                res.append('->'.join([str(i) for i in path]))

            if root.left:
                backtrack(root.left)
            if root.right:
                backtrack(root.right)
            
            path.pop()
        backtrack(root)
        return res