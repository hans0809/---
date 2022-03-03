# 二叉树中节点的前驱和后继的定义：
# 二叉树中某节点的前驱：二叉树中序遍历序列中，某节点的前一个节点
# 二叉树中某节点的后继：二叉树中序遍历序列中，某节点的后一个节点


############################################## 首先建立一棵二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
node4=TreeNode(4)
node5=TreeNode(5)
node6=TreeNode(6)
node7=TreeNode(7)

root=node1
root.left=node2
root.right=node3
root.parent=None

root.left.left=node4
root.left.right=node5
root.left.left.parent=root.left
root.left.right.parent=root.left

root.right.left=node6
root.right.right=node7
root.right.left.parent=root.right
root.right.right.parent=root.right

"""
     1
  2     3
4   5 6   7
"""

#################################################中序遍历
# 1)准备一个栈，首先将整个左侧边界入栈
# 2)当左侧到底时，出栈一个节点并访问，然后继续在该节点的右子树上执行1)
def in_order(root):
    if not root:
        return []

    stack=[]
    res=[]
    while stack or root:
        if root:
            stack.append(root)
            root=root.left#一直往左走，吃左边界
        else:
            root=stack.pop()
            res.append(root.val)
            root=root.right
    print("非递归中序遍历结果为：",res)
    return res
in_order(root)
# 中序遍历为：[4,2,5,1,6,3,7]


#################################################求二叉树中某节点的后继

# 1)如果节点x有右树，那么x的后继就是右树上最左侧的节点
"""
    x                                        x 
        1(最左，是x的后继)                         1 
                                                2
            2                                 3(最左，是x的后继) 
"""
# 2)如果节点x没有右树，那么x就沿着其parent指针向上走，当x是某一个节点m的左树上的最后(右)一个节点时，停，m就是x的后继
"""
            7                                                7  
        6(x是6的左树上的最后（右）一个节点，于是6就是x的后继)      6(x是6的左树上的最后（右）一个节点，于是6就是x的后继)
    3                                                       x      
       5
          x

"""
# 【注意】：整棵树最右侧的节点没有后继，因为此时的节点属于2)，但是这个节点不是某个节点m的左树，
# 就更谈不上是这个节点是某个节点m左树上的最后(右)一个节点了
"""
    6
 3    4
        5(没有后继)
"""

def getSuccessorNode(node):
    if not node:
        return
    
    #1)如果节点x有右树，那么x的后继就是右树上最左侧的节点
    if node.right:
        node=node.right
        while node.left:#一直往左走，就能走到最左侧
            node=node.left
        return node
    #2)如果节点x没有右树，那么x就沿着其parent指针向上走，当x是某一个节点m的左树上的最后(右)一个节点时，停，m就是x的后继
    else:
        parent=node.parent
        while parent:
            # 只要node不是其parent的左孩子(是右孩子)
            if node!=parent.left:
                #就一直向上
                node=parent
                parent=node.parent
            else:#找到啦，停！
                break
        #退出while有两种条件：node=parent.left(找到了非空后继，直接break)，或者parent为空（此时传入的node是最右侧的节点，即上面【注意】中的内容）
        return parent
"""

     1
  2     3
4   5 6   7
"""
# 中序遍历为：[4,2,5,1,6,3,7]
print("************测试求二叉树中节点的后继******************")
print('node3的后继为：',getSuccessorNode(node3).val)#7
print('node1的后继为：',getSuccessorNode(node1).val)#6
print('node4的后继为：',getSuccessorNode(node4).val)#2
print('node7的后继为：',getSuccessorNode(node7))#None
                 




#################################################求二叉树中某节点的前驱

# 把上面求节点后继的代码逻辑反过来，就是求节点的前驱的代码了

def getPreNode(node):
    if not node:
        return
    
    #1)如果节点x有左树，那么x的后继就是左树上最右侧的节点
    if node.left:
        node=node.left
        while node.right:#一直往右走，就能走到最右侧
            node=node.right
        return node
    #2)如果节点x没有左树，那么x就沿着其parent指针向上走，当x是某一个节点m的右树上的最左一个节点时，停，m就是x的前驱
    else:
        parent=node.parent
        while parent:
            # 只要node不是其parent的右孩子(是左孩子)
            if node!=parent.right:
                #就一直向上
                node=parent
                parent=node.parent
            else:#找到啦，停！
                break
        #退出while有两种条件：node=parent.right(找到了非空后继，直接break)，或者parent为空（此时传入的node是最左侧的节点）
        return parent
"""

     1
  2     3
4   5 6   7
"""
# 中序遍历为：[4,2,5,1,6,3,7]
print("************测试求二叉树中节点的前驱******************")
print('node3的前驱为：',getPreNode(node3).val)#6
print('node1的前驱为：',getPreNode(node1).val)#5
print('node4的前驱为：',getPreNode(node4))#None
print('node7的前驱为：',getPreNode(node7).val)#3

