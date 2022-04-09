# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ret=-1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order(root):
            if not root:
                return
            if len(res)!=k:
                in_order(root.left)
                
            res.append(root.val)
            if len(res)==k:
                self.ret=root.val
                return
                
            if len(res)!=k:
                in_order(root.right)
        res=[]
        
        in_order(root)
        return self.ret