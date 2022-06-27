# 求解一元一次方程的正整数解

# 输入描述:
# 输入一行表示该一元一次方程，其中未知数为X，方程包含加法、减法、乘法。

# 字符串长度少于20个字符，保证为合法方程。

# 所有整数绝对值不超过10000000。

# 输出描述:
# 如果X有唯一正整数解，输出该答案。如果解为非正整数、不存在或解不唯一，输出-1。

# 输入例子1:
# 2*X=6

# 输出例子1:
# 3

# 输入例子2:
# X+2*X=3*X

# 输出例子2:
# -1

# 例子说明2:
# 解不唯一

#  对于一元一次方程来说，解不唯一的情况是，出现0=0。其余情况都是有唯一解的，即aX=b，解为b/a

# 系数有可能是3*6这种，比如2*X+2*3=2*13，坑！！！

def iter(s):
    n=len(s)

    x_num=0#X的系数
    xishu=0#常数项

    i=0
    while i <n:
        if s[i] in '+-*':
            i+=1
            continue
        #处理X的系数为１被省略时的情况，系数不为１时，X前面一定是＊，这种情况交给else分支处理
        elif s[i]=='X':
            if i==0:
                x_num+=1
            else:
                if s[i-1]=='+':
                    x_num+=1
                elif s[i-1]=='-':
                    x_num-=1
            i+=1
        else:#s[i]是数字，此时可能是X的系数，也可能是常数项
            if i!=0:
                op=s[i-1]
            else:
                op='+'
            number=int(s[i])
            while i+1<n and s[i+1] not in '+-*X':
                number=number*10+int(s[i+1])
                i+=1
            # 有可能是两(多)个数字相乘
            while i+1<n and s[i+1]=='*' and i+2<n and s[i+2] not in '+-*X':
                number2=int(s[i+2])
                i+=2
                while i+1<n and s[i+1] not in '+-*X':
                    number2=number2*10+int(s[i+1])
                    i+=1
                number=number*number2


            if i+1<n:
                if s[i+1]=='*':#此时一定有i+2<n and s[i+2]=='X
                    if op=='+':
                        x_num+=number
                    elif op=='-':
                        x_num-=number
                else:
                    if op=='+':
                        xishu+=number
                    elif op=='-':
                        xishu-=number
            else:
                xishu+=number
        
            i+=1
    
    return x_num,xishu

def get_cut_point(s):
    n=len(s)
    for i in range(n):
        if s[i]=='=':
            return i

def run(s):
    index=get_cut_point(s)#等号所在下标
    left_x_num,left_xishu=iter(s[0:index])
    right_x_num,right_xishu=iter(s[index+1:])
    x_num=left_x_num-right_x_num
    xishu=right_xishu-left_xishu
    # print(left_x_num,left_xishu,right_x_num,right_xishu)
    if x_num==xishu==0:#多个解
        return -1
    if xishu/x_num==int(xishu/x_num) and xishu/x_num>0:
        return int(xishu//x_num)
    else:
        return -1

while True:
    try:
        s=input()
        res=run(s)
        print(res)
    except:
        break