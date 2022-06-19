# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
# 如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def run(start,end):
            # 此时说明此子树节点数量<=1 ，无需判别正确性，因此直接返回 true
            if start>=end:
                return True
            
            # 按照后续遍历的顺序，end其实就是根节点的值

            p=start
            while postorder[p]<postorder[end]:
                p+=1
            #此时p来到右子树的第一个节点
            index=p
            # postorder[0...index]是左子树，postorder[index...end-1]是右子树,
            # postorder[end]是根节点

            while postorder[p]>postorder[end]:
                p+=1
            
            return p==end and run(start,index-1) and run(index,end-1)
        return run(0,len(postorder)-1)
