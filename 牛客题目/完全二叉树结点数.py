# 给定一棵完全二叉树的头节点head，返回这棵树的节点个数。
class Solution:
    def nodeNum(self , root) -> int:
        # write code here
        # 求树高
        def getHeight(root):
            cnt=0
            while root:
                cnt+=1
                root=root.left
            return cnt
        def getNum(root):
            if not root:
                return 0
            leftHeight=getHeight(root.left)
            rightHeight=getHeight(root.right)
            if leftHeight==rightHeight:
                # 左子树是满二叉树
                return (2**leftHeight-1)+1+getNum(root.right)# 左子树结点个数+根结点1个+右子树结点个数
            else:# leftHeight>rightHeight
                # 右子树是满二叉树
                return getNum(root.left)+1+(2**rightHeight-1)# 左子树结点个数+根结点1个+右子树结点个数
        return getNum(root)