# 小团想要编写一个程序，希望可以统计在M和N之间（M<N，且包含M和N）有多少个六位数ABCDEF满足以下要求：

# (1) ABCDEF这六个数字均不相同，即A、B、C、D、E和F表示六个不同的数字。

# (2) AB+CD=EF。即将这个六位数拆成三个两位数，使得第1个和第2个两位数的和等于第3个两位数。

def check(num):
    nums=[]
    # print(num)
    while num:# 把当前的6位数num拆成一位一位的形式
        nums.append(num%10)
        num//=10
    # print(nums)

    # 必须是6个不同的数
    if len(set(nums))!=6:
        return False

    if ((nums[-1]*10+nums[-2])+(nums[-3]*10+nums[-4]))==(nums[-5]*10+nums[-6]):
        return True
    return False
def run(M,N):
    ans=0
    for num in range(M,N+1):
        if check(num):
            ans+=1
    return ans

while True:
    try:
        m,n=map(int,input().split(' '))
        ans=run(m,n)
        print(ans)
    except:
        break