# 已知两颗二叉树，将它们合并成一颗二叉树。
# 合并规则是：都存在的结点，就将结点值加起来，否则空的位置就由另一个树的结点来代替。

class Solution:
    def mergeTrees(self , t1 ,t2) :
        # write code here
        if not t1 and not t2:
            return None
        elif not t1:
            return t2
        elif not t2:
            return t1
        # 此时t1和t2都不为空
        t1.val=t1.val+t2.val
        t1.left=self.mergeTrees(t1.left,t2.left)
        t1.right=self.mergeTrees(t1.right,t2.right)

        return t1