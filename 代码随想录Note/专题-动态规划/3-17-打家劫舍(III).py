# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
# 这个地区只有一个入口，我们称之为“根”。 
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
# 一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。


# 一棵二叉树，
# 如果选择偷当前结点，那么就不能偷当前结点的左右孩子结点(孩子结点的孩子结点可以偷)，所偷到的价值=当前结点的值
# 如果选择不偷当前结点，那么就可以偷左右孩子节点，所偷到的价值=max(偷左孩子,不偷左孩子) + max(偷右孩子，不偷右孩子)

# 定义dp, dp长度为2，dp[0]代表不偷当前结点能获得的最大价值，dp[1]代表偷当前结点能获得的最大价值

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def do_rob(root):
            if not root:
                return [0,0]#[不偷当前结点能够获得最大价值 ,偷当前结点能够获得最大价值 ]
            
            # 后序遍历

            # left_dp[0]代表不偷当前结点的左孩子结点能获得的最大价值，left_dp[1]代表偷当前结点的左孩子结点能获得的最大价值
            left_dp=do_rob(root.left)
            #right_dp[0]代表不偷当前结点的左孩子结点能获得的最大价值，right_dp[1]代表偷当前结点的左孩子结点能获得的最大价值
            right_dp=do_rob(root.right)


        #不偷当前结点能够获得最大价值 = 偷or不偷左孩子结点能够获得的价值的较大值 + 偷or不偷右孩子结点能够获得的价值的较大值
            val1=max(left_dp) + max(right_dp)

        #偷当前结点能够获得的最大价值 = 当前结点的价值 + 不偷左孩子结点能够获得的价值 + 不偷右孩子结点能够获得的价值
            val2=root.val+left_dp[0]+right_dp[0]

            return [val1,val2]#[不偷当前结点能够获得最大价值 ,偷当前结点能够获得最大价值 ]
        
        result=do_rob(root)
        return max(result)   