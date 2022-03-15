# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue=[]
        queue.append(root)
        depth=1
        while queue:
            size=len(queue)
            for _ in range(size):
                cur =queue.pop(0)
                if not cur.left and not cur.right:
                    return depth
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            depth+=1

#DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth_left,min_depth_right=10000000000,1000000000000
        if root.left:
            min_depth_left=self.minDepth(root.left)
        if root.right:
            min_depth_right=self.minDepth(root.right)
        return 1+min(min_depth_left,min_depth_right)
            