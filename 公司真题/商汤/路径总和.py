# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。
# 判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val==targetSum
        
        def process(root,targetSum):
            if not root:
                return targetSum==0
            
            if not root.left and not root.right:
                return root.val==targetSum
            
            left=False
            right=False
            if root.left:
                left=process(root.left,targetSum-root.val)
            if root.right:
                right=process(root.right,targetSum-root.val)
            
            return left or right
        
        return process(root,targetSum)

# 写复杂了，来个简单的
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val==targetSum
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)