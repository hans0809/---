# 给定两个整数数组preorder和inorder，表示一个二叉树的前序遍历和中序遍历，重构出原二叉树。假设二叉树的节点值没有重复，二叉树节点的定义已经给出。

# 输入例子1:
# [3,9,20,15,7],[9,3,15,20,7],5

# 输出例子1:
# {3,9,20,#,#,15,7}

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 二叉树构造
# @param preorder int整型一维数组 前序遍历
# @param inorder int整型一维数组 中序遍历
# @param length int整型 节点数量
# @return TreeNode类

class Solution:
    def constructTree(self , preorder , inorder , length ):
        # write code here
        if not preorder:
            return 
        root=TreeNode(preorder[0])

        index=inorder.index(preorder[0])

        left_inorder=inorder[:index]
        right_inorder=inorder[index+1:]
        left_preorder=preorder[1:index+1]
        right_preorder=preorder[index+1:]


        root.left=self.constructTree(left_preorder, left_inorder, len(left_inorder))
        root.right=self.constructTree(right_preorder, right_inorder,len(right_inorder))

        return root