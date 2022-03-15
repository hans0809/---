# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root=root
        # 生成中序遍历序列
        self.seq=[0]
        def in_order(root):
            if not root:
                return
                
            in_order(root.left)
            self.seq.append(root.val)
            in_order(root.right)
        in_order(root)
        
        self.cnt=0
            
    def next(self) -> int:
        self.cnt+=1
        return self.seq[self.cnt]


    def hasNext(self) -> bool:
        return len(self.seq)-1>self.cnt
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()