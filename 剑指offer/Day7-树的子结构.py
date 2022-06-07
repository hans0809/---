# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

# B是A的子结构， 即 A中有出现和B相同的结构和节点值。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:        
        def recu(root1,root2):
            # 这里如果B为空，说明B已经访问完了，确定是A的子结构
            if not root2:
                return True
            # 如果B还有节点没比较，而A已经么有可以比较的节点了，那么B不是A的子树
            # 或者A与B的当前节点值不同，那么B也不是A的子树
            if not root1 or root1.val != root2.val:
                return False
            # 继续前序遍历看看A和B的左右子树是否也满足条件，全部满足则返回True
            return recu(root1.left,root2.left) and recu(root1.right,root2.right)
        
        if not B or not A:
            return False
        # A和B的根节点值相同，从A和B的根节点开始做前序遍历
        # or B是A的左子树的子树 
        # or B是A的右子树的子树

        return recu(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)