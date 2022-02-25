# 给定一个二叉树root和一个值 sum ，判断是否有从根节点到叶子节点的节点值之和等于 sum 的路径。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#回溯法:感觉其实并不是真正的回溯，因为sn+=root.val后，后面就不会再对这个根结点操作了
class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        # write code her
        sums=[]
        def pre_order(root,sn):
            if not root:
                return 
            # 开始回溯
            sn+=root.val
            # 如果来到叶子节点，就找到了一条路径，将此时的 路径组成值 添加到结果列表sums中
            if not root.left and not root.right and sn==sum:
                sums.append(sn)

            pre_order(root.left,sn)
            pre_order(root.right,sn)
            
            # 恢复回溯前的状态
            sn-=root.val

        sn=0
        pre_order(root,sn)
        print(sums)
        for i in sums:
            if i==sum:
                return True
        return False

# 回溯法：不记录每一条路径
class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        # write code her
        def pre_order(root,sn):
            if not root:
                return False
            # 开始回溯
            sn+=root.val
            # 来到叶子节点
            if not root.left and not root.right and sn==sum:
                return True

            l_find=pre_order(root.left,sn)
            r_find=pre_order(root.right,sn)
            
            # 恢复回溯前的状态
            sn-=root.val
            return l_find or r_find

        sn=0
        return pre_order(root,sn)

# 直接递归：直接把sn-=root.val 删掉就是了，这个函数后面都没再用到sn
class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        # write code her
        def pre_order(root,sn):
            if not root:
                return False
            sn+=root.val
            # 来到叶子节点
            if not root.left and not root.right and sn==sum:
                return True

            l_find=pre_order(root.left,sn)
            r_find=pre_order(root.right,sn)
            return l_find or r_find
        sn=0
        return pre_order(root, sn)

# 直接递归更直接的是这个写法
class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        # write code her
        if not root:
            return False
        sum-=root.val
        # 来到叶子节点
        if not root.left and not root.right and sum==0:
            return True

        l_find=self.hasPathSum(root.left,sum)
        r_find=self.hasPathSum(root.right,sum)
        return l_find or r_find
# 或者这样
class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        # write code her
        if not root:
            return False
        
        # 来到叶子节点
        if not root.left and not root.right and sum-root.val==0:
            return True

        l_find=self.hasPathSum(root.left,sum-root.val)
        r_find=self.hasPathSum(root.right,sum-root.val)
        return l_find or r_find