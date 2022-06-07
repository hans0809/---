# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。

# 无论是DFS还是BFS，思路都是：对于每一个遍历到的节点，交换其左右子树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root
        
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)

        root.left,root.right=root.right,root.left

        return root

# BFS
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root
        
        
        queue=[root]

        while queue:
            size=len(queue)
            for _ in range(size):
                cur_node=queue.pop()

                cur_node.left,cur_node.right =cur_node.right,cur_node.left

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        
        return root