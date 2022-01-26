# 1)假设以X为根节点，假设可以向X的左树和右树要任何信息
# 2)在上一步的假设下，讨论以X为根节点的树，得到答案的可能性:通常的一个分类是：最终答案是否与根结点有关
# 3)列出所有可能性后，确定到底需要向左树和右树要什么信息
# 4)把左树和右树信息求全(并)集，就是任何一棵子树都需要返回的信息S
# 5)递归函数都返回S，每一棵子树都这么要求
# 6)写代码，在代码中考虑如何把左树信息和右树信息整合出整棵树的信息

############################################## 首先建立一棵二叉树
from operator import le


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root=TreeNode(5)
root.left=TreeNode(2)
root.right=TreeNode(7)
root.left.left=TreeNode(1)
root.left.right=TreeNode(4)
root.right.left=TreeNode(6)
root.right.right=TreeNode(8)

"""
     5
  2     7
1   4 6   8
"""



# 题目1：给定一棵二叉树的根节点root，判断这棵二叉树是不是平衡二叉树

# 平衡二叉树需要满足：左树平衡，右树平衡，左右子树高度超差不超过1

def isBalanced(root):
    is_balanced,height=judge(root)
    return is_balanced

def judge(root):
    if not root:
        is_balanced = True#是否平衡
        height=0#树的高度
        return is_balanced,height

    #子树是否平衡，子树的高度
    left_is_balanced,left_height=judge(root.left)
    right_is_balanced,right_height=judge(root.right)

    # 整棵树的高度
    height=max(left_height,right_height)+1

    #整棵树是否平衡：左树平衡，右树平衡，左右子树高度超差不超过1
    is_balanced=False
    if left_is_balanced and right_is_balanced and abs(left_height-right_height)<=1:
        is_balanced=True
    
    return is_balanced,height
print("#####题目1：判断是否是平衡二叉树#####")
print(isBalanced(root))

    
# 题目2：给定一棵二叉树的根节点root，任何两个节点之间都存在距离，求这棵树的最大距离

# 所有可能性：
# (1)与根结点无关，最大距离=max(左树最大距离，右数最大距离)
# (2)与根结点有关，左树高度+1+右树高度

def getMaxDistance(root):
    max_distance,height=cal_max_distance(root)
    return max_distance
def cal_max_distance(root):
    if not root:
        max_distance=0#最大距离
        height=0#树的高度
        return max_distance,height
    
    # 子树的最大距离，子树的高度
    left_max_distance,left_height=cal_max_distance(root.left)
    right_max_distance,right_height=cal_max_distance(root.right)

    # 整棵树的高度
    height=max(left_height,right_height)+1

    # 整棵树的最大距离
    max_distance=max(
        max(left_max_distance,right_max_distance),# 可能性1：与根结点无关
        left_height+1+right_height                # 可能性2：与根结点有关
    )

    return max_distance,height
print("#####题目2：求二叉树的最大距离#####")
print(getMaxDistance(root))



# 题目3：给定一棵二叉树的根节点root，求这棵二叉树中最大的二叉搜索树所含节点个数

def getMaxBST(root):
    # 返回：
    # 以root为根的二叉树的最大值，最小值，
    # 以root为根的二叉树是否整体是二叉搜索树，
    # 以root为根的二叉树中最大的二叉搜索树所含节点个数(题目所求)
    max_node,min_node,is_all_bst,max_sub_bst_size=process(root)
    return max_node,min_node,is_all_bst,max_sub_bst_size

def process(root):
    if not root:
        return None
    # 这里之所以返回null是因为空树的最大/小值不好写
    # 所以在后面单独处理空树的情况

    #子树的最大/小值，子树整体是否是二叉搜索树，子树中最大的二叉搜索树所含节点个数
    left_info=process(root.left)#左树可能为空
    left_max_node,left_min_node,left_is_all_bst,left_max_sub_bst_size= left_info if left_info else [None]*4 
    right_info=process(root.right)#右树可能为空
    right_max_node,right_min_node,right_is_all_bst,right_max_sub_bst_size=right_info if right_info else [None]*4

    #整棵树的最大/小值
    max_node,min_node=root.val,root.val
    if left_info:
        max_node=max(max_node,left_max_node)
        min_node=min(min_node,left_min_node)
    if right_info:
        max_node=max(max_node,right_max_node)
        min_node=min(min_node,right_min_node)


    #整棵树中最大的二叉搜索树所含节点个数，整棵树整体是否是二叉搜索树
    # 可能性1：与根结点无关。此时整棵二叉树整体不是二叉搜索树(is_all_bst=False)
    is_all_bst=False
    max_sub_bst_size=0
    if left_info:
        max_sub_bst_size=left_max_sub_bst_size
    if right_info:
        max_sub_bst_size=max(max_sub_bst_size,right_max_sub_bst_size)
    # 可能性2：与根结点有关。此时整棵二叉树整体是二叉搜索树(is_all_bst=True)
    # 整棵二叉树都是二叉搜索树需要满足：左右子树都是二叉搜索树，并且左子树最大值<根结点的值<右子树的最小值
    # (同时注意子树是空树的情况，默认空树是二叉搜索树，子树是空树的话就不用考比较值的大小了)
    if (True if not left_info else left_is_all_bst) \
        and (True if not right_info else right_is_all_bst) \
        and (True if not left_info else left_max_node<root.val) \
        and (True if not right_info else right_min_node>root.val):
        #整棵树中最大的二叉搜索树所含节点个数
        max_sub_bst_size=(0 if not left_info else left_max_sub_bst_size)\
            +1\
            +(0 if not right_info else right_max_sub_bst_size)
        #整棵树整体是二叉搜索树
        is_all_bst=True
    
    return max_node,min_node,is_all_bst,max_sub_bst_size
print("#####题目3：求二叉树中最大二叉搜索树所含节点数#####")
print(getMaxBST(root))



# 题目4：给定一棵二叉树的根节点root，求这棵二叉树中最大的二叉搜索树的根结点
def getMaxBSTHead(root):
    # 返回：
    # 以root为根的二叉树的最大值，最小值，
    # 以root为根的二叉树中最大的二叉搜索树所含节点个数
    # 以root为根的二叉树中最大的二叉搜索树的根(头节点)
    max_node,min_node,max_sub_bst_head,max_sub_bst_size=process1(root)
    print("最大二叉搜索树的根结点是:",max_sub_bst_head.val)
    return max_sub_bst_head
def process1(root):
    if not root:
        return None
    
    # 子树的最大/小值，子树中最大的二叉搜索树所含节点个数，子树中的最大的二叉搜索树的根(头节点)
    left_info=process1(root.left)
    left_max_node,left_min_node,left_max_sub_bst_head,left_max_sub_bst_size=left_info if left_info else [None]*4
    right_info=process1(root.right)
    right_max_node,right_min_node,right_max_sub_bst_head,right_max_sub_bst_size=right_info if right_info else [None]*4

    # 整棵树的最大/小值，整棵树中最大的二叉搜索树所含节点个数，子树中的最大的二叉搜索树的根(头节点)
    max_node,min_node=root.val,root.val
    if left_info:
        max_node=max(max_node,left_max_node)
        min_node=min(min_node,left_min_node)
        # 可能性1：与根结点无关。此时整棵二叉树整体不是二叉搜索树
        max_sub_bst_head=left_max_sub_bst_head
        max_sub_bst_size=left_max_sub_bst_size
    if right_info:
        max_node=max(max_node,right_max_node)
        min_node=min(min_node,right_min_node)
        # 可能性1：与根结点无关。此时整棵二叉树整体不是二叉搜索树
        if right_max_sub_bst_size>max_sub_bst_size:
            max_sub_bst_size=right_max_sub_bst_size
            max_sub_bst_head=right_max_sub_bst_head
    
    # 可能性2：与根结点有关，此时整棵树都是二叉搜索树
    if (True if not left_info else left_max_sub_bst_head==root.left) \
        and (True if not right_info else right_max_sub_bst_head==root.right) \
        and (True if not left_info else left_max_node<root.val) \
        and (True if not right_info else right_min_node>root.val):
        # 此时当前整棵树整体是二叉搜索树
        max_sub_bst_head=root
        #当前整棵树中最大的二叉搜索树所含节点个数就是当前整个以root为根的二叉树的节点数
        max_sub_bst_size=(0 if not left_info else left_max_sub_bst_size)\
            +1\
            +(0 if not right_info else right_max_sub_bst_size) 

    return max_node,min_node,max_sub_bst_head,max_sub_bst_size
print("#####题目3：求二叉树中最大二叉搜索树的根节点#####")
print(getMaxBSTHead(root))# 5

    


# 题目5：整个公司的人员结构可以看作是一棵标准的多叉树。
# 树的头节点是公司唯一的老板，除老板外，每个员工都有唯一的直接上级，
# 叶节点是没有任何下属的基层员工，除基层员工外，每个员工都有一个或多个直接下级，另外每个员工都有一个快乐值。
# 这个公司现在要办 party，你可以决定哪些员工来，哪些员工不来。但是要遵循如下的原则：
# 1.如果某个员工来了，那么这个员工的所有直接下级都不能来。
# 2.派对的整体快乐值是所有到场员工快乐值的累加。
# 3.你的目标是让派对的整体快乐值尽量大。
# 给定一棵多叉树，请输出派对的最大快乐值。

###########先建立一棵这样的多叉树
class Company:
    def __init__(self, val=0, nexts=[]):
        self.val = val#快乐值
        self.nexts = nexts#下级所有员工
node1=Company(1)
node2=Company(2)
node3=Company(3)
node4=Company(4)
node5=Company(5)
node6=Company(6)
node7=Company(7)

node1.nexts=[node2,node3,node4]
node4.nexts=[node5,node6,node7]
"""
          1
   2      3       4 
               5  6  7
"""

# 简单例子分析所有可能性：
"""
   root
a    b    c
"""   
# 可能性1：根结点来，那么最大快乐值就等于根结点的快乐值
# 可能性2：根结点不来，那么最大快乐值就等于0+max(a来，a不来)+max(b来，b不来)+max(c来，c不来)

def HappyValue(root):
    if not root:
        return 0
    
    # 来或不来对应的快乐值，返回最大的
    yes_value,no_value=cal_happy_value(root)
    return max(yes_value,no_value)
def cal_happy_value(root):
    #如果是叶子节点(最底层的员工)，那么来的快乐值就是他本身的快乐值val
    # 不来的快乐值是0，因为他没有下一级员工了
    if len(root.nexts)==0:
        return root.val,0
    
    yes=root.val#当前root来对应的快乐值
    no=0#当前root不来对应的快乐值显然是0
    for next in root.nexts:
        cur_yes,cur_no=cal_happy_value(next)
        yes+=cur_no#root来，那么最大快乐值就等于根结点的快乐值
        no+=max(cur_yes,cur_no)#root不来，那么最大快乐值就等于0+max(a来，a不来)+max(b来，b不来)+max(c来，c不来)
    return yes,no
print("#####题目5：派对的最大快乐值#####")
print(HappyValue(node1))#2,3,5,6，7,来，其余不来


# 题目6：判断一棵二叉树是否是满二叉树

# 关键：满二叉树满足 2^树高-1=节点总数

def isFull(root):
    if not root: 
        return True
    
    height,nodes_num=do(root)
    res=2**height-1==nodes_num
    if res:
        print("是满二叉树")
    else:
        print("不是满二叉树")
def do(root):
    if not root: 
        height=0#树的高度
        nodes_num=0#树的节点数
        return height,nodes_num
    
    #求左右子树的树高，树节点数
    left_height,left_nodes_num=do(root.left)
    right_height,right_nodes_num=do(root.right)

    # 整棵树的高度，节点数
    height=1+max(left_height,right_height)
    nodes_num=1+left_nodes_num+right_nodes_num

    return height,nodes_num
print("#####题目6：判断是否是满二叉树#####")
isFull(root)#是满二叉树


# 题目7：判断一棵二叉树是否是完全二叉树

# 可能性1：整棵树是满二叉树，此时左右子树都是满二叉树，且左树高度=右树高度
"""
           *
       *       *
     *   *   *   *
"""
# 可能性2：整棵树不是满二叉树，此时有3种情况下可以保证整棵树是完全二叉树
# 1)左子树是完全二叉树，右子树是满二叉树，左树高度=右树高度+1
"""
           *
       *       *
     *   *   *   *
   *
"""
# 2)左子树是满二叉树，右子树是完全二叉树，左树高度=右树高度
"""
           *
       *       *
     *   *   *   
"""
# 3)左子树是满二叉树，右子树是满二叉树，左树高度=右树高度+1
"""
           *
       *       *
     *   *     
"""
def isComplete(root):
    # 是否是满二叉树，子树是否是完全二叉树，树的高度
    isFull,isCBT,height=is_complete(root)
    return isCBT
def is_complete(root):
    if not root:
        return True,True,0
    
    # 子树是否是完全二叉树，子树是否是满二叉树，子树的高度
    left_isFull,left_isCBT,left_height=is_complete(root.left)
    right_isFull,right_isCBT,right_height=is_complete(root.right)

    # 整棵树的高度
    height=1+max(left_height,right_height)

    # 整棵树是否是满二叉树，整棵树是否是完全二叉树
    isFull=left_isFull and right_isFull and left_height==right_height
    isCBT=False
    if isFull:
        isCBT=True
    else:
        if (left_isCBT and right_isFull and left_height==right_height+1) \
        or (left_isFull and right_isCBT and left_height==right_height) \
        or (left_isFull and right_isFull and left_height==right_height+1):
            is_CBT=True
    return isFull,isCBT,height

print("#####题目7：判断是否是完全二叉树: 递归#####")
print(isComplete(root))#True

# 题目7还可以用层序遍历的方式解题
# 如果一棵二叉树是完全二叉树，那么它一定满足：
# 1) 任何一个节点，如果它只有右子树而没有左子树，那么这二叉树一定不是完全二叉树
# 如果1)不满足，那么执行2)： 
# 2) 一旦遍历到的某个节点只有左孩子或者左右孩子都没有，
#    那么它后面遍历到的节点必须全是叶子节点，否则不是这棵二叉树一定完全二叉树

# 层序遍历
def isComplete_BFS(root):
    if not root:
        return True

    queue=[]
    queue.append(root)

    #是否遇到了 2)遍历到的某个节点只有左孩子或者左右孩子都没有
    leaf=False

    while queue:
        current_node=queue.pop(0)
        # 遇到了 1)只有右孩子而没有左孩子，那么这二叉树一定不是完全二叉树
        if not current_node.left and current_node.right:
            return False
        # 遇到了 2)曾经遍历到某个节点只有左孩子或者左右孩子都没有，
        # 且当前遍历到的节点不是叶子节点，那么这二叉树一定不是完全二叉树
        if leaf and (current_node.left or current_node.right):
            return False
        
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        
        # 遍历到了某个节点只有左孩子或者左右孩子都没有
        if (not root.left) or (not root.right):
            leaf=True

    return True
print("#####题目7：判断是否是完全二叉树: 层序遍历#####")
print(isComplete_BFS(root))

# 题目8：求二叉树的最大深度
# 就是求一棵二叉树的树高
def maxDepth(root):
    depth=max_depth(root)
    return depth
def max_depth(root):
    if not root:
        return 0
    
    # 左右子树的最大深度
    left_depth=max_depth(root.left)
    right_depth=max_depth(root.right)

    # 整棵树的最大深度
    depth=1+max(left_depth,right_depth)

    return depth
print("#####题目8：求二叉树的最大深度#####")
print(maxDepth(root))

# 题目9：求二叉树的最小深度，即从根结点到叶子节点的最短路径长度
def minDepth(root):
    min_depth=get_min_depth(root)
    return min_depth
def get_min_depth(root):
    if not root:
        return 0
    
    # 求左右子树的最小深度
    left_min_depth=get_min_depth(root.left)
    right_min_depth=get_min_depth(root.right)

    #求整棵树的最小深度
    # 如果左右子树都为空
    if not root.left and not root.right:
        min_depth=1
    # 如果左右子树都不为空
    elif root.left and root.right:
        min_depth=1+min(left_min_depth, right_min_depth)
    # 如果只有左子树为空
    elif not root.left and root.right:
        min_depth=1+right_min_depth
    # 如果只有右子树为空
    elif root.left and not root.right:
        min_depth=1+left_min_depth

    return min_depth
print("#####题目9：求二叉树的最小深度#####")
print(minDepth(root))    



# 题目10：给定一棵二叉树的根结点，以及树中的两个节点a和b，求a和b的最低公共祖先

# 方法1：递归

# a和b都不在树中
# a和b当中只有一个在树中
# 这两种情况都找不到交汇点，无公共祖先，返回None

# a和b都不是根结点，都在以根结点为头的树上：
# 1) a和b一左一右
# 2) a和b都在左侧
# 2) a和b都在右侧
# a和b当中有且只有一个就是根结点

def lowestAncestor(root,o1,o2):
    ans,find1,find2=ancestor(root,o1,o2)
    return ans
def ancestor(root,o1,o2):
    if not root:
        # o1和o2在子树中的最初交汇点，子树中是否发现有o1/o2
        return None,False,False
    
    # o1和o2在子树中的最初交汇点，子树中是否发现有o1/o2
    left_ans,left_find1,left_find2=ancestor(root.left,o1,o2)
    right_ans,right_find1,right_find2=ancestor(root.right,o1,o2)

    # 整棵树中是否发现有o1/o2
    if root==o1 or left_find1 or right_find1:
        find1=True
    else:
        find1=False
    if root==o2 or left_find2 or right_find2:
        find2=True
    else:
        find2=False
    
    # o1和o2在整棵树中的最初交汇点，即两者的最近公共祖先
    ans=None
    #  三个if只会运行一个

    # 在左树上已经提前交汇了
    if left_ans:
        ans=left_ans
    # 在右树上已经提前交汇了
    if right_ans:
        ans=right_ans
    # 此时没有在左树或右树上提前交汇，但又发现o1和o2找全了，
    # 那么一定在当前root节点交汇
    if ans is None:
        if find1 and find2:
            ans=root
    
    return ans,find1,find2
print("#####题目10：求二叉树中两个节点的最近公共祖先(递归解法)#####")
print(lowestAncestor(root,root.left.left,root.right).val)


# 方法2：哈希表
# 遍历二叉树，记录每一个节点对应的父节点
# 
def lowestAncestor2(root,o1,o2):
    if not root:
        return None
    
    parent_map=dict()
    parent_map[root]=None#根结点没有父节点
    # 遍历填表
    fillParentMap(root,parent_map)

    # 开始找最近公共祖先
    o1_set=set()
    cur=o1
    o1_set.add(cur)

    # 从o1一直往上走，直到来到根结点
    while parent_map.get(cur) is not None:
        cur=parent_map.get(cur)
        o1_set.add(cur)
    
    cur=o2
    while cur not in o1_set:
        cur=parent_map.get(cur)
    
    return cur   
# 遍历填表
def fillParentMap(root,parent_map):
    if root.left:
        parent_map[root.left]=root
        fillParentMap(root.left,parent_map)
    if root.right:
        parent_map[root.right]=root
        fillParentMap(root.right,parent_map)
print("#####题目10：求二叉树中两个节点的最近公共祖先(哈希表解法)#####")
print(lowestAncestor2(root,root.left.left,root.right).val)


# 题目11：给定一个非负整数n，代表二叉树的节点个数。返回能形成多少种不同的二叉树结构(与值无关，只看结构)。

# 方法1：暴力递归
def numBts(n):
    if n<0:
        return 0
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    
    res=0
    # 根结点始终占一个
    # 遍历左子树节点数的所有可能
    for leftNum in range(n):
        # 左子树能够形成的不同二叉树的个数
        leftWays=numBts(leftNum)
        rightNum=n-leftNum-1# 此时对应的右子树节点数
        # 右子树能够形成的不同二叉树的个数
        rightWays=numBts(rightNum)
        res+=leftWays*rightWays# 整体能够形成的不同二叉树的个数，用乘法
    return res
n=3
print('能够形成不同二叉树的个数：',numBts(n))
# for n in range(4):
#     print(numBts(n))

# 方法2：动态规划
def numBts2(n):
    if n<0:
        return 0
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    
    # dp[i]:共i个节点时, 能够形成的不同的二叉树结构的总数
    dp=[0 for _ in range(n+1)]
    dp[0]=1

    # 遍历填表
    for totalNum in range(1,n+1):
        for leftNum in range(totalNum):
            dp[totalNum]+=dp[leftNum]*dp[totalNum-leftNum-1]
    #print(dp)
    return dp[n]
n=3
print('能够形成不同二叉树的个数：',numBts2(n))


# 题目12：二叉树每个节点都有一个int型权值，给定一棵二叉树，要求计算出从根结点到叶节点的所有路径中，权值和最大的值为多少

# 二叉树的递归套路解法
def maxDis(root):
    if not root:
        return 0
    return max_dis(root)
def max_dis(root):
    # 叶子节点
    if not root.left and not root.right:
        return root.val
    # 求从子树的根结点(如果存在)出发到叶子节点的最大路径(权值)和mdis
    mdis=0
    if  root.left:
        mdis=max_dis(root.left)
    if  root.right:
        mdis=max(mdis,max_dis(root.right))
    # 返回整棵树的根结点权值+子树mdis就是答案
    return root.val+mdis
print('从根结点到叶子节点的最大权值为：',maxDis(root))
# 另外一种解法
maxSum=0
def maxDis2(root):
    p(root,0)
    return maxSum
def p(root,pre):
    global maxSum
    # pre:从根结点出发，到当前节点的上一节点的最大路径(权值)和
    if not root.left and not root.right:#叶子节点
        maxSum=max(maxSum, pre+root.val)
    if root.left:
        p(root.left,pre+root.val)
    if root.right:
        p(root.right,pre+root.val)
print('从根结点到叶子节点的最大权值为：',maxDis2(root))

# 如果改成最小路径和呢？很简单
def minDis(root):
    if not root:
        return 0
    return min_dis(root)
def min_dis(root):
    # 叶子节点
    if not root.left and not root.right:
        return root.val
    # 求从子树的根结点(如果存在)出发到叶子节点的最大路径(权值)和mdis
    mdis=0
    if  root.left:
        mdis=min_dis(root.left)
    if  root.right:
        mdis=min(mdis,min_dis(root.right))
    # 返回整棵树的根结点权值+子树mdis就是答案
    return root.val+mdis
print('从根结点到叶子节点的最小权值为：',minDis(root))