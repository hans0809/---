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