# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归的两种写法
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root,ssum):
            if not root:
                return False
            ssum+=root.val
            # 来到叶子结点
            if not root.left and not root.right:
                return ssum==targetSum 
            return helper(root.left,ssum) or helper(root.right,ssum)
            
        return helper(root,0) 


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum==root.val
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)

# 非递归
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
        queue_node=[root]
        queue_val=[root.val]
        while queue_node:
            cur_node=queue_node.pop(0)
            cur_val=queue_val.pop(0)
            # 来到叶子结点
            if not cur_node.left and not cur_node.right:
                if cur_val==targetSum:
                    return True
                    
            if cur_node.left:
                queue_node.append(cur_node.left)
                queue_val.append(cur_val+cur_node.left.val)
            if cur_node.right:
                queue_node.append(cur_node.right)
                queue_val.append(cur_val+cur_node.right.val)
        return False
                
        