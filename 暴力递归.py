# 题目1：假设有排成一行的N个位置，记为1~N，N一定大于或等于2
# 开始时机器人在其中的M位置上(M一定是1~N中的某一个)
# 如果机器人来到1位置，那么下一步只能来到2位置
# 如果机器人来到N位置，那么下一步只能来到N-1位置
# 如果在其它位置，则下一步可以往左走或者往右走
# 规定机器人必须走K步，最终能来到P位置(P也是1~N中的一个)的方法总共有几种？
# 给定4个参数N,M,K,P，返回方法数

# 暴力递归
def ways1(N,M,K,P):
    # 参数无效直接返回0
    if N<2 or K<1 or M<1 or M>N or P<1 or P>N:
        return 0
    
    return walk1(N,M,K,P)
def walk1(N,cur,rest,P):
    """
    N:位置为1~N，固定参数
    cur:当前在cur位置，可变参数
    rest:还剩rest步没走，可变参数
    P:目标位置，固定参数
    """
    if rest==0:
        return 1 if cur==P else 0
    # 来到边界
    if cur==1:
        return walk1(N,2,rest-1,P)
    if cur==N:
        return walk1(N,N-1,rest-1,P)
    # 没来到边界，可以向左走，也可以向右走
    return walk1(N,cur-1,rest-1,P)+walk1(N,cur+1,rest-1,P)
N,M,K,P=5,2,6,4
print(ways1(N,M,K,P))
    


# 加数组作为缓存(记忆化搜索)
def ways2(N,M,K,P):
    # 参数无效直接返回0
    if N<2 or K<1 or M<1 or M>N or P<1 or P>N:
        return 0

    #把所有(cur,rest)加入缓存
    #dp=[[-1]*(K+1) for _ in range(N+1)]
    dp=[[-1 for _ in range(K+1)] for _ in range(N+1)]
    # 上面两种写法都可以，但是写成dp=[[-1]*(K+1)]*(N+1)就不对，为什么？

    def walk2(N,cur,rest,P):
        if dp[cur][rest]!=-1:
            return dp[cur][rest]

        ans=0
        if rest==0:
            ans=1 if cur==P else 0

        elif cur==1:
            ans=walk2(N,2,rest-1,P)
   
        elif cur==N:
            ans=walk2(N,N-1,rest-1,P)
 
        else:
            ans=walk2(N,cur-1,rest-1,P)+walk2(N,cur+1,rest-1,P)

        dp[cur][rest]=ans
        return ans
    res=walk2(N,M,K,P)
    return res
N,M,K,P=5,2,6,4
print(ways2(N,M,K,P))


# 加哈希表作为缓存(记忆化搜索)
def ways3(N,M,K,P):
    # 参数无效直接返回0
    if N<2 or K<1 or M<1 or M>N or P<1 or P>N:
        return 0
    dic=dict()
    return walk3(N, M,K,P,dic)
def walk3(N,cur,rest,P,dic):
    """
    N:位置为1~N，固定参数
    cur:当前在cur位置，可变参数
    res:还剩rest步没走，可变参数
    P:目标位置，固定参数
    """

    # 已经在缓存中，直接返回
    if (cur,rest) in dic:
        return dic[(cur,rest)]

    #不在缓存中，就先计算出来，然后加入缓存
    if rest==0:
        dic[(cur,rest)]=1 if cur==P else 0
        return dic[(cur,rest)]
    # 来到边界
    if cur==1:
        dic[(cur,rest)] = walk3(N,2,rest-1,P,dic)
        return dic[(cur,rest)]
    if cur==N:
        dic[(cur,rest)] = walk3(N,N-1,rest-1,P,dic)
        return dic[(cur,rest)]
    # 没来到边界，可以向左走，也可以向右走
    dic[(cur,rest)] = walk3(N,cur-1,rest-1,P,dic)+walk3(N,cur+1,rest-1,P,dic)
    return dic[(cur,rest)]
N,M,K,P=5,2,6,4
print(ways3(N,M,K,P))

# 动态规划
"""
N=7
M=2
K=5
P=3
    rest  0     1    2    3    4    5
cur         
 0        X     X    X    X    X    X   
 1        0     0    1    0    3    0
 2        0     1    0    3    0    9
 3        1     0    2    0    6    0
 4        0     1    0    3    0    10
 5        0     0    1    0    4    0
 6        0     0    0    1    0    5
 7        0     0    0    0    1    0

"""
# 根据记忆化搜索方法，写出动态规划
# 外层循环遍历列rest，内层循环遍历行cur，不能改顺序，因为有依赖关系
def ways4(N,M,K,P):
    if N<2 or K<1 or M<1 or M>N or P<1 or P>N:
        return 0 

    dp=[[0 for _ in range(K+1)] for _ in range(N+1)]

    # 剩余步数rest为0时来到了目标位置P，于是找到一种方法
    # 第0列除了第P行外，其余取值都是默认的0
    dp[P][0]=1
    
    # 处理剩余步数rest取值是1...K的情况
    for rest in range(1,K+1):
        # 来到左边界
        # 当前位于1位置，只能向2位置走，
        # 即：等于其左下角的元素值
        dp[1][rest]=dp[2][rest-1]

        # 非边界，此时cur取值为2...N-1
        # 即：等于其左上角的元素值+左下角的元素值
        for cur in range(2,N):
            dp[cur][rest]=dp[cur-1][rest-1]+dp[cur+1][rest-1]
        
        # 来到右边界
        # 当前位于N位置，只能向N-1位置走
        # 即：等于其左上角的元素值
        dp[N][rest]=dp[N-1][rest-1]
    
    return dp[M][K]
N,M,K,P=5,2,6,4
print(ways4(N,M,K,P))



# 动态规划常用的4种尝试模型
# 1) 从左往右的尝试模型
# 2) 范围上的尝试模型
# 3) 多样本位置全对应的尝试模型
# 4) 寻找业务限制的尝试模型







# 题目2：求字符串的所有子序列

def getSubs(s):
    ans = []
    path=[]
    get_subs(s,0,ans,path)
    return ans
def get_subs(s,index,ans,path):
    if index == len(s):
        ans.append(path[:])
        return
    
    # 不加入当前index的字符
    no=path[:]
    get_subs(s,index+1,ans,no)

    # 加入当前index的字符
    yes=path[:]+[s[index]]
    get_subs(s,index+1,ans,yes)

print('代码1-字符串"aac:的所有子序列为：',getSubs('aac'))


def getSubs2(s):
    ans = []
    path=[]
    get_subs2(s,0,ans,path)
    return ans
def get_subs2(s,index,ans,path):
    if index == len(s):
        ans.append(path[:])
        return
    
    # 不加入当前index的字符
    get_subs2(s,index+1,ans,path)

    # 加入当前index的字符
    path.append(s[index])
    get_subs2(s,index+1,ans,path)
    path.pop()
print('代码2-字符串"aac:的所有子序列为：',getSubs2('aac'))


# 题目3：求字符串的所有子序列，要求子序列不能含有重复字符
# 比如上一题"aac"的子序列中，答案之一'aa'在本题是不合法的
def getSubs3(s):
    ans = []
    path=[]
    get_subs3(s,0,ans,path)
    return ans
def get_subs3(s,index,ans,path):
    if index == len(s):
        ans.append(path[:])
        return
    
    # 不加入当前index的字符
    get_subs3(s,index+1,ans,path)

    # 加入当前index的字符
    if s[index] not in path:
        path.append(s[index])
        get_subs3(s,index+1,ans,path)
        path.pop()
print('字符串"aac:的所有不重复子序列为：',getSubs3('aac'))


# 题目4：给定一个字符串，求全排列
def Permutation(s):
    res=[]
    if not s:
        return res
    s=list(s)
    permutation(s,0,res)
    return res
# s[0..i-1]已经做好决定的
# s[i...]都有机会来到i位置
# 如果i是终止位置，s当前的样子，就是一种结果
def permutation(s,i,res):
    if i==len(s):
        res.append(s[:])
        return
    # 如果i没有终止，那么i后面位置的元素的都有机会来到i位置
    for j in range(i,len(s)):
        swap(s,i,j)#j位置元素来到i位置
        permutation(s,i+1,res)
        swap(s,i,j)#恢复现场
def swap(s,i,j):
    s[i],s[j]=s[j],s[i]

print('字符串"aac"的所有全排列为：',Permutation('aac'))

# 题目5：给定一个字符串，求不重复的全排列

# 一个方法是，直接用上题的方法，然后去重即可

# 另一个是分支限界法(提前杀死某些分支)：
# 用一个辅助数组或者哈希表记录以某个字符开头的全排列结果是否已经被加入res，如果是，就跳过
def Permutation2(s):
    res=[]
    if not s:
        return res
    s=list(s)
    permutation2(s,0,res)
    return res
# s[0..i-1]已经做好决定的
# s[i...]都有机会来到i位置
# 如果i是终止位置，s当前的样子，就是一种结果
def permutation2(s,i,res):
    if i==len(s):
        res.append(s[:])
        return
    visited=dict()
    # 如果i没有终止，那么i后面位置的元素的都有机会来到i位置
    for j in range(i,len(s)):
        if s[j] not  in  visited:
            visited[s[j]]=True
            swap2(s,i,j)#j位置元素来到i位置
            permutation2(s,i+1,res)
            swap2(s,i,j)#恢复现场
def swap2(s,i,j):
    s[i],s[j]=s[j],s[i]
print('字符串"aac"的所有不重复全排列为：',Permutation2('aac'))



# 题目6：从左往右的尝试模型1：规定1和A对应，2和B对应，...,11和K对应,...,
# 那么一个字符串比如"111"就可以转化为"AAA","KA"和"AK"
# 给定一个只有数字字符组成的字符串，返回有多少种转化结果

def getNumber(s):
    if not s:
        return 0
    s=list(s)
    return get_number(s,0)
# 第0...index-1号字符已经转化好了
# 看index...能够获得多少种转化结果
def get_number(s,i):
    # i来到了终止位置，得到一种转化方案
    if i==len(s):
        return 1
    
    # i没有到终止位置
    if s[i]=='0':#'0'没有对应字符，没有转化方案
        return 0
    
    # 字符s[i]不是'0'
    if s[i]=='1':
        res=get_number(s,i+1)
        if i+1<len(s):
            res+=get_number(s,i+2)
        return res
    if s[i]=='2':
        res=get_number(s,i+1)
        if i+1<len(s) and '0'<=s[i+1]<='6':
            res+=get_number(s,i+2)
        return res
    
    # s[i] in '3'~'9'
    return get_number(s,i+1)
    
print("字符串{}转化后有{}种可能".format("11101",getNumber("11101")))#后面的101只能拆成10 1，前面的11可以转成AA 或者K，因此共2种转化结果

# 改成动态规划
def dpWay_getNumber(s):
    if not s:
        return 0
    s=list(s)
    n=len(s)# 数字字符串长度

    dp=[0 for _ in range(n+1)]
    dp[n]=1# 找到一种方案
    for i in range(n-1,-1,-1):
        if s[i]=='0':
            dp[i]=0
        elif s[i]=='1':
            dp[i]=dp[i+1]
            if i+1<n:
                dp[i]+=dp[i+2]
    
        elif s[i]=='2':
            dp[i]=dp[i+1]
            if i+1<n and '0'<= s[i+1]<='6':
                dp[i]+=dp[i+2]
 
        # s[i] in '3'~'9' 
        else: 
            dp[i]=dp[i+1]
        # if s[i]=='0':
        #     dp[i]=0
        # if s[i]=='1':
        #     dp[i]=dp[i+1]
        #     if i+1<n:
        #         dp[i]+=dp[i+2]
    
        # if s[i]=='2':
        #     dp[i]=dp[i+1]
        #     if i+1<n and '0'<= s[i+1]<='6':
        #         dp[i]+=dp[i+2]
 
        # # s[i] in '3'~'9' 
        # if '3'<=s[i]<='9':
        #     dp[i]=dp[i+1]
    return dp[0]
print("字符串{}转化后有{}种可能(动态规划解法)".format("11101",dpWay_getNumber("11101")))#后面的101只能拆成10 1，前面的11可以转成AA 或者K，因此共2种转化结果



# 题目7：从左往右的尝试模型2：给定两个长度都为N的数组weights和values
# weights[i]和values[i]分别代表第i号物品的重量和价值
# 给定一个整数bag，代表一个载重为bag的袋子
# 你装的物品不能超过这个重量，返回能装下的最多价值是多少

def getMaxValue(w,v,bag):
    return get_max_value(w,v,0,0,bag)
# 第0...index-1号货物已经做了选择(拿还是不拿)，使得已经达到的重量是alreadyW
# 求拿or不拿第index...号物品能够获得的最大价值
def get_max_value(w,v,index,alreadyW,bag):
    """
    w，v，bag不变
    index：第i个物品的下标i
    alreadyW: 此时背包中已经放入的物品的总重量
    """

    # 装不下了，此方案无效，最大价值用-1返回
    if alreadyW>bag:
        return -1
    
    #  重量没超
    # 但没物品可拿了，第index...号物品对应的最大价值是0
    if index==len(w):
        return 0
    
    # 有物品可拿
    #不拿第index个物品能够获得最大价值p1
    p1=get_max_value(w,v,index+1,alreadyW,bag)
    #拿第index个物品能够获得的最大价值p2
    p2next=get_max_value(w,v,index+1,alreadyW+w[index],bag)
    p2=-1
    if p2next!=-1:
        p2=p2next+v[index]
    return max(p1,p2)
w=[1,2,30]
v=[5,6,7]
bag=12
print('能够获得最大价值：',getMaxValue(w,v,bag))

# 也可以在进入递归函数之前就判断是否超过袋子承受重量，超过了就不去递归了，更改代码如下
def getMaxValue1(w,v,bag):
    return get_max_value(w,v,0,0,bag)
# 第0...index-1号货物已经做了选择(拿还是不拿)，使得已经达到的重量是alreadyW
# 求拿or不拿第index...号物品能够获得的最大价值
def get_max_value1(w,v,index,alreadyW,bag):
    """
    w，v，bag不变
    index：第i个物品的下标i
    alreadyW: 此时背包中已经放入的物品的总重量
    """
    
    #  重量没超
    # 但没物品可拿了，第index...号物品对应的最大价值是0
    if index==len(w):
        return 0
    
    # 有物品可拿
    #不拿第index个物品能够获得最大价值p1
    p1=get_max_value1(w,v,index+1,alreadyW,bag)
    #拿第index个物品能够获得的最大价值p2
    p2=-1
    if alreadyW+w[index]<=bag:# 这里保证了重量不会超
        p2=v[index]+get_max_value1(w,v,index+1,alreadyW+w[index],bag)

    return max(p1,p2)

w=[1,2,30]
v=[5,6,7]
bag=12
print('能够获得最大价值：',getMaxValue1(w,v,bag))

# 把上述解法改成动态规划
"""
3件物品，背包容量是4
初始化表格如下：
     0   1   2   3   4       alreadyW     
 0                   0
 1                   0
 2                   0
 3   0   0   0   0   0
index
"""
def dpWay1(w,v,bag):
    n=len(w)
    dp=[[0 for _ in range(bag+1)] for _ in range(n+1)]
    #dp[n][:]=0# 最后一行初始化为0：没物品了
    #dp[:][bag]=0# 已经使用了bag空间，剩余背包容量为0，最大价值总是0

    for index in range(n-1,-1,-1):
        for alreadyW in range(bag-1,-1,-1):
            # 不拿第index件物品能够获得的最大价值
            p1=dp[index+1][alreadyW]
            p2=-1
            if alreadyW+w[index]<=bag:
                p2=v[index]+dp[index+1][alreadyW+w[index]]
            dp[index][alreadyW]=max(p1,p2)
    return dp[0][0]
print('动态规划-能够获得最大价值(代码1)',dpWay1(w,v,bag))


def getMaxValue2(w,v,bag):
    return get_max_value2(w,v,0,bag)
# 只剩下rest的空间了
# index...货物自由选择拿还是不拿，但是剩余空间rest不要小于0
# 返回index...能够获得的最大价值
def get_max_value2(w,v,index,rest):
    """
    rest:背包bag剩余空间
    """

    # 背包没空间了，无效方案
    if rest<=0:
        return -1
    
    # 背包有空间
    # 没物品可拿了，index...的最大价值是0
    if index==len(w):
        return 0

    # 不拿第index号物品，index..获得的最大价值是p1
    p1=get_max_value2(w,v,index+1,rest)

    # 拿第index号物品，index..获得的最大价值是p2
    p2=-1
    p2next=get_max_value2(w,v,index+1,rest-w[index])
    if p2next!=-1:
        p2=p2next+v[index]
    
    return max(p1,p2)

print('能够获得最大价值(代码2)：',getMaxValue(w,v,bag))

# 把上述解法改成动态规划
"""  
3件物品，背包容量是4
初始化表格如下：
      0   1   2   3   4  rest
  0   0
  1   0
  2   0
  3   0   0   0   0   0
index
"""
def dpWay2(w,v,bag):
    n=len(w)# 物品数
    dp=[[0 for _ in range(bag+1)] for _ in range(n+1)]
    #dp[n][:]=0# 最后一行初始化为0：没物品了
    #dp[:][0]=0#第0列初始化为0：背包容量为0时，价值为0

    for index in range(n-1,-1,-1):
        for rest in range(1,bag+1):
            # 不拿第index件物品能获得的最大价值
            p1=dp[index+1][rest]
            # 拿第index件物品能获得的最大价值
            p2=-1
            if rest-w[index]>=0:
                p2=v[index]+dp[index+1][rest-w[index]]
            dp[index][rest]=max(p1,p2)
    return dp[0][bag]
            
print('动态规划-能够获得最大价值(代码2)',dpWay2(w,v,bag))







# 题目8：范围上的尝试模型：给定一个整型数组arr，代表数值不同的纸牌排成一条线，
# 玩家A和玩家B依次拿走每张纸牌，规定A先拿，B后拿，但是每个玩家每次只能拿走最左或最右的纸牌，
# 玩家A和B都绝顶聪明，请返回最后获胜者的分数

def winnerScore(arr):
    if not arr:
        return 0
    return max(first(arr,0,len(arr)-1), 
                second(arr,0,len(arr)-1))
# 先手
def first(arr,L,R):
    if L==R:
        return arr[L]
    return max(arr[L]+second(arr,L+1,R),
                arr[R]+second(arr,L,R-1))
# 后手
def second(arr,L,R):
    # 只有一张纸牌，由于是后手，
    # 所以这唯一的一张纸牌被先手拿走，后手什么也拿不到
    if L==R:
        return 0
    # 先手肯定想尽一切办法给后手留下小的，
    # 后手只能被动接受，所以取最小的
    return min(first(arr,L+1,R),
                first(arr,L,R-1))

print("博弈游戏胜者的分数：",winnerScore([1,100,7]))#100  

# 改成动态规划
"""
建立两张二维表，初始化如下：其中x表示此处不合法，因为L不能超过R

s:
   0  1  2   L
0  1  x  x 
1    100 x
2        7
R



f:
   0  1  2   L
0  0  x  x 
1     0  x
2        0
R

"""
def dpWay_winnerScore(arr):
    if not arr:
        return 0
    
    n=len(arr)
    f=[[0 for _ in range(n)] for _ in range(n)]
    s=[[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        f[i][i]=arr[i]
        s[i][i]=0
    
    for i in range(1,n):
        # 按对角线方式进行填值
        L=0
        R=i
        while L<n and R<n:
            f[L][R]=max(arr[L]+s[L+1][R],arr[R]+s[L][R-1])
            s[L][R]=min(f[L+1][R],f[L][R-1])
            L+=1
            R+=1
    return max(f[0][n-1],s[0][n-1])
print("dp-博弈游戏胜者的分数：",dpWay_winnerScore([1,100,7]))#100  



# 题目9：凑零钱，给一个数组，包含不同面值的钱，和一个总钱数，
# 求凑成总钱数的总的方法数，数组中每一个面值的钱可以无限次使用

# 方法1：暴力递归
def ways1(arr,aim):
    if not arr or aim<0:
        return 0
    return process1(arr,0,aim)
# 可以自由使用arr[index...]中的所有面值，每一种面值都可以使用任意张
# 组成rest，有多少种方法
# 假设arr[0]=1，那么可枚举拿arr[0]的张数，从0开始，比如0，1，2，3，...
# 直到张数*arr[0]>rest
def process1(arr,index,rest):
    # 没面值可以用了
    if index==len(arr):
        return 1 if rest==0 else 0
    ans=0
    zhang=0
    while zhang*arr[index]<=rest:
        ans+=process1(arr,index+1,rest-zhang*arr[index])
        zhang+=1
    return ans
arr=[5,10,50,100]
aim=1000
print('凑零钱方法数为：',ways1(arr,aim))

# 方法2：记忆化搜索
def ways2(arr,aim):
    if not arr or aim<0:
        return 0
    n=len(arr)
    dp=[[-1 for _ in range(aim+1)] for _ in range(n+1)] 
    return process2(arr,0,aim,dp)
def process2(arr,index,rest,dp):
    if dp[index][rest]!=-1:
        return dp[index][rest]
    
    if index==len(arr):
        dp[index][rest]=1 if rest==0 else 0
        return dp[index][rest]
    
    ans=0
    zhang=0
    while zhang*arr[index]<=rest:
        ans+=process2(arr,index+1,rest-zhang*arr[index],dp)
        zhang+=1
    dp[index][rest]=ans# 加入缓存
    return ans
arr=[5,10,50,100]
aim=1000
print('记忆化搜索-凑零钱方法数为：',ways2(arr,aim))

# 方法3：动态规划
""" 
初始化如下：
   0 1 2 3 ... 1000  aim
0
1
2
3
4  1 0 0 0 ...  0
index

"""
def ways3(arr,aim):
    if not arr or aim<0:
        return 0
    n=len(arr)
    dp=[[-1 for _ in range(aim+1)] for _ in range(n+1)] 

    dp[n][0]=1
    for col in range(1,aim+1):
        dp[n][col]=0
    
    for index in range(n-1,-1,-1):
        for rest in range(0,aim+1):
            ans=0
            zhang=0
            while zhang*arr[index]<=rest:
                ans+=dp[index+1][rest-zhang*arr[index]]
                zhang+=1
            dp[index][rest]=ans

    return dp[0][aim]
arr=[5,10,50,100]
aim=1000
print('动态规划-凑零钱方法数为：',ways3(arr,aim))

# 方法4：优化动态规划
def ways4(arr,aim):
    if not arr or aim<0:
        return 0
    n=len(arr)
    dp=[[-1 for _ in range(aim+1)] for _ in range(n+1)] 

    dp[n][0]=1
    for col in range(1,aim+1):
        dp[n][col]=0
    
    for index in range(n-1,-1,-1):
        for rest in range(0,aim+1):
            dp[index][rest]=dp[index+1][rest]
            if rest-arr[index]>=0:
                dp[index][rest]+=dp[index][rest-arr[index]]

    return dp[0][aim]
print('优化的动态规划-凑零钱方法数为：',ways4(arr,aim))


# 题目9扩展：凑零钱，给一个数组，包含不同面值的钱，和一个总钱数，
# 求凑成总钱数的总的方法数，数组中每一个面值的钱**只能使用一次**

# 暴力递归(代码好像有问题)
def ways1(arr,aim):
    if not arr or aim<0:
        return 0
    return process1(arr,0,aim)
# 可以自由使用arr[index...]中的所有面值，每一种面值只能使用一次
# 组成rest，有多少种方法

def process1(arr,index,rest):

    if rest<0:
        return 0

    # 没面值可以用了
    if index==len(arr):
        return 1 if rest==0 else 0

    # 不使用第index个面值的钱，方法数
    not_use_index_ans=process1(arr,index+1,rest)
    
    # 使用第index个面值的钱，方法数
    use_index_ans=0
    for i in range(index,len(arr)):
        if rest-arr[index]>=0:
            use_index_ans=process1(arr,index+1,rest-arr[index])
            break
        # 如果没进if，那么use_index_ans=0(中开头的if rest<0: return 0)

    ans=use_index_ans+not_use_index_ans
    return ans

arr=[500,300,900,100,2,22,123,700,98,346]
aim=1000
print('[变种]凑零钱方法数为：',ways1(arr,aim))


# 多样本位置全对应的尝试模型
# 题目10：求两个字符串的最长公共子序列。比如str1="abc123e",str2="s123d"，则答案为"123"
# 解法：弄一张[len(str1),len(str2)]的表dp，dp[i][j]代表str1[...i]和str2[...j]的最长公共子序列
# 总共分4种情况：
# 1)str1[...i]和str2[...j]的最长公共子序列既不以str1[i]结尾，也不以str2[j]结尾，此时dp[i][j]=dp[i-1][j-1]
# 2)str1[...i]和str2[...j]的最长公共子序列以str1[i]结尾，不以str2[j]结尾，此时dp[i][j]=dp[i][j-1]
# 3)str1[...i]和str2[...j]的最长公共子序列不以str1[i]结尾，以str2[j]结尾，此时dp[i][j]=dp[i-1][j]
# 4)str1[...i]和str2[...j]的最长公共子序列既以str1[i]结尾，又以str2[j]结尾，此时dp[i][j]=dp[i-1][j-1]+1
# 注：[...i]等价于[0...i]
# 初始时会将第0行和第0列做初始化

def lcse(str1,str2):
    n1,n2=len(str1),len(str2)
    dp=[[0 for _ in range(n2)] for _ in range(n1)]
    dp[0][0]=1 if str1[0]==str2[0] else 0
    # 初始化第0列
    for i in range(1,n1):
        dp[i][0]=max(dp[i-1][0],1 if str1[i]==str2[0] else 0)
    # 初始化第0行
    for j in range(1,n2):
        dp[0][j]=max(dp[0][j-1],1 if str1[0]==str2[j] else 0)
    # 计算剩余位置
    for i in range(1,n1):
        for j in range(1,n2):
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])# 处理情况2)和3)
            if str1[i]==str2[j]:# 情况4，若命中，则此时最长公共子序列的长度一定比情况1(dp[i][j]=dp[i-1][j-1])大，因此可以省略和情况1的比较
                dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1)
            # 注意：下面的else可以省略，因为情况2)中的dp[i-1][j]和情况3中的dp[i][j-1]
            # 都会依赖到情况1中的dp[i-1][j-1]，因此情况2)和情况3)的结果不可能比情况1)小，所以不要再考虑情况1了
            else:# 若情况4没命中，则考虑情况1
                dp[i][j]=max(dp[i][j],dp[i-1][j-1])
    return dp[n1-1][n2-1]+1
str1="abcde11"
str2="ace11"
print('最长公共子序列长度为：',lcse(str1,str2))


# 业务限制的模型(同时也是从左往右的尝试模型，但是有业务上的限制)

# 题目11：给定一个数组arr(按时间有序)，代表每个人喝完咖啡准备刷杯子的时间点，
# 只有一台咖啡机，一次只能洗一个杯子，时间耗费a，洗完才能洗下一杯，
# 每个咖啡杯也可以自己挥发干净，时间耗费b，咖啡杯可以并行挥发，
# 返回让所有咖啡杯变干净的最早完成时间

# 暴力递归：
# washLine表示洗咖啡的机器可用的时间点，
# 假设drinks[0...index-1]都已经洗干净了，
# 现在只需要考虑drinks[index...]都想变干净，返回所需最少时间对应的时间点

def solve(drinks,a,b):
    return process(drinks,a,b,0,0)
def process(drinks,a,b,index,washLine):
    # 只剩最后一杯了
    if index ==len(drinks)-1:
        # 用机器洗或挥发掉，选最早结束的
        return min(
            max(washLine,drinks[index])+a,#用机器洗，最早结束时间。有可能在wsahLine时间点第index个咖啡还没喝完，得等喝完，也就是drinks[index]时间带你才能开始洗，花费时间为a
            drinks[index]+b)# 挥发，喝完时间点为drinks[index]，挥发花费时间为b
    # 剩余不止一杯咖啡
    # 1) 用机器洗,drinks[index...]都想变干净，所需最少时间对应的时间点是p1
    # wash是洗完第index杯时的时间点
    wash=max(washLine,drinks[index])+a
    # 递归求解第index+1...杯(drinks[index+1...])洗干净的最早时间点
    next1=process(drinks,a,b,index+1,wash)# 第index杯用了机器洗，所以占用时间从washLine到wash，机器从wash这个时间点可用
    p1=max(wash,next1)
    #2) 自己挥发，drinks[index...]都想变干净，所需最少时间对应的时间点是p2
    dry=drinks[index]+b# 挥发完的时间点是dry
    # 递归求解第index+1...杯(drinks[index+1...])洗干净的最早时间点
    next2=process(drinks,a,b,index+1,washLine)# 第index杯不用机器洗，所以不占用时间，机器仍从washLine这个时间点可用
    p2=max(dry,next2)

    # 取最小的
    return min(p1,p2)
drinks=[1,1,5,5,7,10,12,12,12,12,12,12,15]
a=3
b=10
print('洗咖啡杯最早结束的时间点：',solve(drinks,a,b))

# 动态规划
def dpSolve(drinks,a,b):
    # 挥发所用时间比机器洗的还快
    if a>=b:
        return drinks[len(drinks)-1]+b
    
    n=len(drinks)
    limit=0# 咖啡机什么时候可用(即开始可用的时间点)
    # 不挥发，全部用机器洗，能够获得limit的最大取值
    for i in range(n):
        limit=max(limit,drinks[i])+a
    
    dp=[[0 for _ in range(limit+1)] for _ in range(n)]
    # 只剩一杯咖啡，对应第n-1行
    for washLine in range(0,limit+1):
        dp[n-1][washLine]=min(
            max(washLine,drinks[n-1])+a,
            drinks[n-1]+b)
    # 计算其余位置(# 剩余不止一杯咖啡)
    for index in range(n-2,-1,-1):
        for washLine in range(0,limit+1):
                
            # 1) 用机器洗,drinks[index...]都想变干净，所需最少时间对应的时间点是p1
            # wash是洗完第index杯时的时间点
            p1=99999999999999999999
            wash=max(washLine,drinks[index])+a
            if wash<=limit:
                next1=dp[index+1][wash]# 递归求解第index+1...杯(drinks[index+1...])洗干净的最早时间点
                p1=max(wash,next1)
            #2) 自己挥发，drinks[index...]都想变干净，所需最少时间对应的时间点是p2
            dry=drinks[index]+b# 挥发完的时间点是dry
            # washLine永远不会超过limit，for循环内层保证了这一点
            next2=dp[index+1][washLine]# 递归求解第index+1...杯(drinks[index+1...])洗干净的最早时间点
            p2=max(dry,next2)#p2也不会超过limit

            dp[index][washLine]=min(p1,p2)

    return dp[0][0]

drinks=[1,1,5,5,7,10,12,12,12,12,12,12,15]
a=3
b=10
print('洗咖啡杯最早结束的时间点：',dpSolve(drinks,a,b))