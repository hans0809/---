# 给定一棵二叉搜索树，请找出其中第 k 大的节点的值。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.vis=[]
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root:
            return

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            self.vis.append(root.val)
            in_order(root.right)
        in_order(root)
        return self.vis[-k]            


# 不开辅助数组的方法
class Solution:
    def __init__(self):
        self.res=None
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root:
            return
         # 中序遍历的倒叙
        def in_order(root):
            if not root:
                return
            in_order(root.right)

            self.k-=1
            if self.k==0:
                self.res=root.val

            in_order(root.left)
        
        self.k=k
        in_order(root)
        return self.res          