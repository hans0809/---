# 针对题目：输入只有一个int，输出也只有一个int.
# 方法：先枚举几个，找出规律，然后优化代码。

# 题目1：小虎去附近的商店买苹果，奸诈的商贩使用了捆绑交易，只提供6个每袋和8个每袋的包装，包装不可拆分。
# 可是小虎现在指向购买签好n个苹果，小虎想购买尽量少的袋数方便携带。日过不能购买恰好n个苹果，小虎将不会购买。
# 输入一个整数n，代表小虎想要买的苹果个数，返回最少使用多少个袋子。如果无论如何都不能装下，返回-1.

# 方法1：类似贪心
def minBags(apple):
    if apple<0:
        return -1
    bag6=-1 # 需要使用装6个的袋子数
    bag8=apple//8 # 需要使用装8个的袋子数

    rest=apple-8*bag8 # 剩余需要装6个的袋子搞定的苹果数

    #while bag8>=0# 都可以，24是6和8的最小公倍数，加了这一判断可以剪枝，因为用bag8只需3个袋子，而用bag6需要4个，前者更少
    while bag8>=0 and rest<=24:
        restUse6=rest/6 if rest%6==0 else -1
        if restUse6!=-1:
            bag6=restUse6
            break
        
        bag8-=1
        rest=apple-8*bag8
    return bag6+bag8 if bag6!=-1 else -1
apple=100
print('最少袋子数：',minBags(apple))

# for apple in range(1000):
#     print(apple,minBags(apple))

# 题目2：先手和后手都绝顶聪明，它们比赛吃草，先手先吃，后手后吃，谁先吃完最后一份草谁就赢
# 吃的草的数量必须是4的幂次，比如1，4，16，64,...
# 给定一共有几份草n，输出两者谁赢：先手赢就输出"先手"，后手赢就输出"后手"。

def getWinner(n):
    # 草的份数：0  1  2  3  4 
    # 谁赢：   后  先 后  先 先
    if n<5:
        return "后手" if n==0 or n==2 else "先手"

    # n>=5时
    base=1# 先手决定吃的草
    while base<=n:
        # 当前一共n份草，先手吃base份，n-base留给后手吃
        if getWinner(n-base)=="后手":
            return "先手"
        # if base>n/4:# Java中防止溢出，Python不需要
        #     break
        base*=4
    return "后手" 
n=6
print('吃草比赛赢家：',getWinner(n))

for n in range(30):
    print(getWinner(n))
# 发现规律：后先后先先 一致循环
# 所以可以改成如下代码：
def getWinner2(n):
    n=n%5
    return "后手" if n==0 or n==2 else "先手"
print('吃草比赛赢家：',getWinner2(n))


