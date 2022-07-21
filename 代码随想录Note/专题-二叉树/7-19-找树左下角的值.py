# 给定一个二叉树，在树的最后一行找到最左边的值。

# 那么如果找最左边的呢？可以使用前序遍历，这样才先优先左边搜索，
# 然后记录深度最大的叶子节点，此时就是树的最后一行最左边的值。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    last_depth=-1
    res=-1
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        def run(root,depth):
            if not root:
                return

            if not root.left and not root.right:
                # 最先遇到的就是左节点，此时已经将last_depth改为当前层的depth，
                # 所以即使右侧再遇到同一层的节点，但由于不满足if判断，所以不会覆盖掉
                if depth>self.last_depth:
                    self.res=root.val
                    self.last_depth=depth
            
            run(root.left,depth+1)
            run(root.right,depth+1)
            
        run(root,0)
        return self.res