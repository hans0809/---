# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
# 第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        elif not root.left and not root.right:
            return [[root.val]]
        
        res=[]

        queue=[root]

        i=1
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
            if i%2==1:
                res.append(tmp)
            elif i%2==0:
                res.append(tmp[::-1])
            
            i+=1
        
        return res