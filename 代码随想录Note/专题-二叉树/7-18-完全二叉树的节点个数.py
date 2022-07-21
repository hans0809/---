# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_height=0
        right_height=0
        
        left,right=root.left,root.right

        while left:
            left_height+=1
            left=left.left
        while right:    
            right_height+=1
            right=right.right
        # 如果相等，那么以root为根节点的数是一棵满二叉树
        if left_height==right_height:
            return pow(2,left_height+1)-1# 加1是因为这里的height是子树的深度，而我们需要得到有根结点的树的深度，所以深度加1
        
        return 1+self.countNodes(root.left)+self.countNodes(root.right)