# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root=TreeNode(preorder[0])
        index=inorder.index(root.val)
        root.left=self.buildTree(preorder[1:1+index],inorder[:index])
        root.right=self.buildTree(preorder[1+index:],inorder[index+1:])
        return root