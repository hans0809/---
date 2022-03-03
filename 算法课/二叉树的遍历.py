# 目录：
# 建树
# 二叉树的前中后序遍历的非递归实现(DFS)
# 二叉树的层序遍历(BFS)
# 求二叉树的宽度。两种写法，第二种更Pythonic
# 二叉树的序列化与反序列化，分别用DFS和BFS实现


############################################## 首先建立一棵二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)
"""
     1
  2     3
4   5 6   7
"""


############################################### 二叉树的非递归遍历

# 先序遍历：根 左 右 
# 1)准备一个栈，然后让根节点入栈
# 2)出栈一个元素，访问它，然后先将其右孩子压入栈，再将其左孩子压入栈(没有孩子可忽略)
# 重复2)，直至栈空

def pre(root):
    if not root:
        return []
    stack=[]
    stack.append(root)

    res=[]
    while stack:
        current_node=stack.pop()
        res.append(current_node.val)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)
    print("非递归前序遍历结果为：",res)
    return res

pre(root)#[1, 2, 4, 5, 3, 6, 7]
    
# 后序遍历：左 右 根
# 前序遍历是 根 左 右，当时是先压入右孩子再压入左孩子
# 那如果反过来，先压入左孩子再压入右孩子，那就变成了 根 右 左
# 根 右 左 倒过来，正好是后续遍历的顺序：左 右 根
# 因此，可以在前序遍历的基础上，调换一下左右孩子入栈的顺序，最后逆序打印就完成了后序遍历
def post(root):
    if not root:
        return []
    stack=[]
    stack.append(root)

    res=[]
    while stack:
        current_node=stack.pop()
        res.append(current_node.val)
        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)
    print("非递归后序遍历结果为：",res[::-1])
    return res[::-1]
post(root)#[4, 5, 2, 6, 7, 3, 1]


# 中序遍历
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



# 层序遍历
def BFS(root):
    if not root:
        return []
    queue=[]
    res=[]

    queue.append(root)

    while queue:
        current_node=queue.pop(0)
        res.append(current_node.val)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    print('层序遍历结果为：',res)
    return res
BFS(root)#[1, 2, 3, 4, 5, 6, 7]


########################################## 基于层序遍历的方法 ，求二叉树的宽度，即：每一层中包含节点个数的最大值
# 代码1：加一个map记录每一个节点的所在层数
def getWidth(root):
    if not root:
        return 0

    queue=[]
    map={}#(节点，节点所在层数)

    queue.append(root)
    map[root]=1#根节点所在层数为1
    
    maxNodes=0#二叉树宽度，最后就返回它
    
    currentLevel=1# 当前正在遍历的层数，初始是根结点所在的第一层，因此初始化为1
    currentLevelNodes=0#记录第level层所含节点个数，遍历时才更新

    while queue:
        current_node=queue.pop(0)
        curLevel=map[current_node]#当前节点所在层数
        #层序遍历的套路
        if current_node.left:
            map[current_node.left] = curLevel+1#下一层节点所在层数要加1
            queue.append(current_node.left)
        if current_node.right:
            map[current_node.right] = curLevel+1#下一层节点所在层数要加1
            queue.append(current_node.right)
        
        # 精彩之处开始
        if curLevel==currentLevel:# 如果当前节点还没去往下一层，那么当前层节点数加1
            currentLevelNodes+=1
        else:#第一次来到下一层
            #更新二叉树宽度
            maxNodes=max(maxNodes,currentLevelNodes)
            #初始化刚刚来到的这下一层所含节点数为1
            currentLevelNodes=1
            #当前正在遍历的层更新为当前层
            currentLevel=curLevel#等价于currentLevel+=1

        #while结束后，最后一层的节点数只是统计完了，但还没来得及和maxNodes作比较更新呢
        maxNodes=max(maxNodes,currentLevelNodes)

    print('方法1求得的二叉树的宽度为：',maxNodes)
    return maxNodes
getWidth(root)


# 代码2：用一个list记录每一层的所有节点
def getWidth2(root):
    if not root:
        return []

    res = []#元素也是一个列表，用于记录每一层的所有节点
    queue = [root]
    while queue:
        # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
        size = len(queue)
        tmp = []
        # 将队列中的元素都拿出来(也就是获取这一层的所有节点)，放到临时list中
        # 如果节点的左/右子树不为空，也放入队列中
        for _ in range(size):
            curNode = queue.pop(0)
            tmp.append(curNode.val)
            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)
        # 将临时list加入
        res.append(tmp)
    width=max([len(nodes) for nodes in res ])

    print('方法2求得的二叉树的宽度为：',width)
    return width
getWidth2(root)


#######################################################二叉树的序列化与反序列化
# 方法1：层序遍历
def serialLeverOrder(root):#序列化
    res=[]#记录序列化结果

    queue=[]
    queue.append(root)

    res.append(root.val)

    while queue:
        current_node=queue.pop(0)

        if current_node.left:
            queue.append(current_node.left)
            res.append(current_node.left.val)
        else:
            res.append(None)
        
        if current_node.right:
            queue.append(current_node.right)
            res.append(current_node.right.val)
        else:
            res.append(None)
    
    print("基于层序遍历，二叉树的序列化结果为：",res)
    return res
serialLeverOrder(root)#[1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, None, None]

def buildSerialLeverOrder(res_list):#反序列化
    #res_list就是序列化的结果，比如[1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, None, None]
    if not res_list:
        return 

    #记录反序列化的结果
    queue=[]

    #建立根结点
    root=TreeNode(res_list.pop(0))

    # 只有当不为空时才加入
    if root:
        queue.append(root)

    while queue:
        current_node=queue.pop(0)

        left=res_list.pop(0)
        if left is not None:
            current_node.left=TreeNode(left)
        else:
            current_node.left=None

        right=res_list.pop(0)
        if right is not None:
            current_node.right=TreeNode(right)
        else:
            current_node.right=None

        # 只有当不为空时才加入
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    # 这样就从序列化的res_list中重建出了二叉树
    # 可以调用层序遍历函数BFS来验证一下反序列化后得到的二叉树的层序遍历结果对不对
    print('基于层序遍历，二叉树的反序列化结果为：',BFS(root))
    return root

#先调用序列化函数serialLeverOrder将二叉树序列化，再调用反序列化函数buildSerialLeverOrder做反序列化
buildSerialLeverOrder(serialLeverOrder(root)) #[1, 2, 3, 4, 5, 6, 7]
    

# 方法2：深度优先遍历，以前序遍历为例(后序也可以，但中序不行)

# 序列化
def preSerialize(root):
    if not root:
        return []

    res=[]
    pre_serialize(root,res)
    print("基于前序遍历，二叉树的序列化结果为：",res)
    return res
def pre_serialize(root,res):
    if root is None:
        res.append(None)
    else:
        res.append(root.val)
        pre_serialize(root.left,res)
        pre_serialize(root.right,res)
preSerialize(root)

# 反序列化
def buildSerialPreOrder(res_list):
    if not res_list:
        return
    
    reverse_res=build_serial_pre_order(res_list)

    # 可以调用上面非递归实现的前序遍历函数pre来验证一下反序列化后得到的二叉树的前序遍历结果对不对
    print("基于前序遍历，二叉树的反序列化结果为：",pre(reverse_res))
    return reverse_res
def build_serial_pre_order(res_list):
    current_val=res_list.pop(0)

    if current_val is None:#base case
        return None

    root=TreeNode(current_val)
    root.left=build_serial_pre_order(res_list)
    root.right=build_serial_pre_order(res_list)
    return root
buildSerialPreOrder(preSerialize(root))#[1, 2, 4, 5, 3, 6, 7]   


