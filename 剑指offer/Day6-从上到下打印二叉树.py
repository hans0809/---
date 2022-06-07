# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。


# 其实就是二叉树的层序遍历
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
            return [root.val]
        
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
            res.extend(tmp)
        
        return res