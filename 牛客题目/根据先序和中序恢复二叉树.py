class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def buildTree(xianxu,zhongxu):
    if not xianxu:
        return
    root=ListNode(xianxu[0])
    index=zhongxu.index(xianxu[0])
    root.left=buildTree(xianxu[1:index+1], zhongxu[:index])
    root.right=buildTree(xianxu[index+1:], zhongxu[index+1:])
    return root