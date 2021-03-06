# 小美是团队的负责人，需要为团队制定工作的计划，以帮助团队产出最大的价值。

# 每周团队都会有两项候选的任务，其中一项为简单任务，一项为复杂任务，两项任务都能在一周内完成。
# 第i周，团队完成简单任务的价值为li，完成复杂任务的价值为hi。
# 由于复杂任务本身的技术难度较高，团队如果在第i周选择执行复杂任务的话，需要在i-1周不做任何任务专心准备。
# 如果团队在第i周选择执行简单任务的话，不需要提前做任何准备。

# 现在小美的团队收到了未来N周的候选任务列表，请帮助小美确定每周的工作安排使得团队的工作价值最大。


# 我的解法：17/20 组用例通过。。。
# 因为这题有个坑: 第1周既可以做简单任务也可以做复杂任务，而我之前的理解是第1周只能做简单任务，因为没有前一周的准备时间啊
# 但这题默认在第一周前已经可以做好充分准备
def run(ls,hs):
    n=len(ls)#n=len(hs)
    #dp[i]:未来第i周能够获得的最大工作价值,i=1,2,...,n
    dp=[0 for _ in range(n+1)]
    # dp[0]无意义

    # (~~划掉~~)初始化：第0周没有准备时间，所以只能选择做简单任务
    # 初始化：第1周可以选择直接做复杂任务，也可以做简单任务
    dp[1]=max(ls[0],hs[0])

    # 从第2周开始，按照正常逻辑计算。。。
    for i in range(2,n+1):
        # 可以选择做简单任务：dp[i]=dp[i-1]+ls[i]
        # 也可以选择做复杂任务(需要提前一周准备，此时前一周啥也不做，)：dp[i]=dp[i-2]+hs[i]
        dp[i]=max(dp[i-1]+ls[i-1], dp[i-2]+hs[i-1])

    return dp[n]

while True:
    try:
        n=int(input())

        if n==0:
            print(0)
            continue

        ls,hs=[],[]
        for _ in range(n):
            cur_l,cur_h=map(int,input().split(' '))
            ls.append(cur_l)
            hs.append(cur_h)

        if n==1:
            print(ls[0])
            continue

        res=run(ls,hs)
        print(res)
    except:
        break

