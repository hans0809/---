# 给定一棵二叉树，你需要计算它的直径长度。
# 一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def cal_max_distance(root):
            if not root:
                max_distance=0#最大距离
                height=0#树的高度
                return max_distance,height
            
            # 子树的最大距离，子树的高度
            left_max_distance,left_height=cal_max_distance(root.left)
            right_max_distance,right_height=cal_max_distance(root.right)

            # 整棵树的高度
            height=max(left_height,right_height)+1

            # 整棵树的最大距离
            max_distance=max(
                max(left_max_distance,right_max_distance),# 可能性1：与根结点无关
                left_height+1+right_height                # 可能性2：与根结点有关
            )

            return max_distance,height
        max_distance,height=cal_max_distance(root)
        return max_distance-1