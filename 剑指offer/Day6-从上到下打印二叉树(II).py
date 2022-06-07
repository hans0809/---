# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        elif not root.left and not root.right:
            return [[root.val]]
        
        res=[]

        queue=[root]
        while queue:
            size=len(queue)
            tmp=[]
            for _ in range(size):
                cur_node=queue.pop(0)
                tmp.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(tmp)
        
        return res