# 对于两个字符串A和B，如果A和B中出现的字符种类相同且每种字符出现的次数相同，则A和B互为变形词，
# 请设计一个高效算法，检查两给定串是否互为变形词。

# 给定两个字符串A和B，请返回一个bool值，代表他们是否互为变形词。


# 输入描述:
# 两行，每行各一个字符串s，s长度小于1000


# 输出描述:
# bool 值

# 输入例子1:
# bcbc
# cbcb

# 输出例子1:
# 1

def check(a,b):
    if set(a)!=set(b):
        return False

    n1,n2=len(a),len(b)
    rec1=dict()
    rec2=dict()
    for i in range(n1):
        if a[i] not in rec1:
            rec1[a[i]]=1
        else:
            rec1[a[i]]+=1
    for i in range(n2):
        if b[i] not in rec2:
            rec2[b[i]]=1
        else:
            rec2[b[i]]+=1
    # print(rec1,'\n',rec2)
    for k,v in rec1.items():
        if k not in rec2 or rec2[k]!=v:
            return False
    
    return True
while True:
    try:
        a=input()
        b=input()
        res=check(a,b)
        print(int(res))
    except:
        break