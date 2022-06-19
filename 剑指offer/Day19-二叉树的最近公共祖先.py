# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def run(root,p,q):
            if not root:
                return None,False,False

            left_ans,left_find_p,left_find_q=run(root.left,p,q)
            right_ans,right_find_p,right_find_q=run(root.right,p,q)

            if root==p or left_find_p or right_find_p:
                find_p=True
            else:
                find_p=False
            if root==q or left_find_q or right_find_q:
                find_q=True
            else:
                find_q=False
            
            ans=None
            if left_ans:
                ans=left_ans
            if right_ans:
                ans=right_ans
            if not ans:
                if find_p and find_q:
                    ans=root
                
            return ans,find_p,find_q

        # p和q在子树中的最初交汇点，子树中是否找到p，子树中是否找到q
        ans,find_p,find_q=run(root,p,q)
        return ans