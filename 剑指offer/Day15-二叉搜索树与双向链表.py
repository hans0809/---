# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
# 要求不能创建任何新的节点，只能调整树中节点指针的指向。


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pre=None
        self.head=None
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        # elif这一部分也可以不写，直接注释掉
        elif not root.left and not root.right:
            root.left=root
            root.right=root
            return root


        def in_order(root):
            if root:
                in_order(root.left)
                if not self.pre:
                    self.head=root
                    root.left=self.pre
                    self.pre=root
                else:
                    self.pre.right=root
                    root.left=self.pre
                    self.pre=root

                in_order(root.right)
        
        in_order(root)
        self.head.left=self.pre
        self.pre.right=self.head
        return self.head