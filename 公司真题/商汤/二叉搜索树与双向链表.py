# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
# 要求不能创建任何新的节点，只能调整树中节点指针的指向。

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        #空
        if not root:
            return
        
        self.pre=None

        # 中序遍历
        def in_order_dfs(cur):
            if not cur:
                return 
            in_order_dfs(cur.left)

            if not self.pre:# 第一个节点
                self.head = cur
                self.pre=cur
            else:
                self.pre.right=cur
                cur.left=self.pre
                self.pre=cur

            in_order_dfs(cur.right)
        
        in_order_dfs(root)

        self.head.left=self.pre
        self.pre.right=self.head

        return self.head