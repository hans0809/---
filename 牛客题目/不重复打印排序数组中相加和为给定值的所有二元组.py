# https://www.nowcoder.com/practice/1ff1a607c81748baa1823ffa687d74c4?tpId=101&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D101&difficulty=&judgeStatus=&tags=&title=&gioEnter=menu

def solve(arr,k):
    n=len(arr)
    i=0
    j=n-1
    while i<j:
        if arr[i]+arr[j]==k:
#             res.append(arr[i],arr[j])
            print(arr[i],arr[j])
            # 去重
            while arr[i]==arr[i+1]:
                i+=1
            while arr[j]==arr[j-1]:
                j-=1
            i+=1
            j-=1
        elif arr[i]+arr[j]<k:
            i+=1
        else:
            j-=1
#接收用户输入的两个整数
n,k = map(int,input().split())
#将n个整数存放到列表中
ls = list(map(int,input().split()))
solve(ls,k)