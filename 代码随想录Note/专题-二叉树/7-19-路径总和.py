# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。
# 判断该树中是否存在 根节点到叶子节点 的路径，
# 这条路径上所有节点值相加等于目标和 targetSum 。
# 如果存在，返回 true ；否则，返回 false 。

# 叶子节点 是指没有子节点的节点。

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def run(root,targetSum):
            if not root:
                return  False
            if not root.left and not root.right:
                return targetSum==root.val
    
            return run(root.left,targetSum-root.val) or run(root.right,targetSum-root.val)
        
        return run(root,targetSum)



# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，
# 找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

# 叶子节点 是指没有子节点的节点。

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path=[]
        res=[]
        def run(root,targetSum):
            if not root:
                return

            path.append(root.val)

            if not root.left and not root.right and targetSum==root.val:
                res.append(path[:])
            
            run(root.left,targetSum-root.val)
            run(root.right,targetSum-root.val)
            path.pop()

        run(root,targetSum)
        return res