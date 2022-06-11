# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，
# 找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

# 叶子节点 是指没有子节点的节点

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
        self.path=[]
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def dfs(root,target):
            if not root:
                return
            
            self.path.append(root.val)
            if not root.left and not root.right:# 叶子节点
                if target==root.val:
                    self.res.append(self.path[:])

            dfs(root.left,target-root.val)
            dfs(root.right,target-root.val)

            self.path.pop()
        dfs(root,target)
        return self.res