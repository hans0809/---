# https://www.nowcoder.com/practice/11b7dd7cbf064900bc664bb5fd4e2fab?tpId=101&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D101&difficulty=&judgeStatus=&tags=&title=&gioEnter=menu
# 只需要固定一个，就变成了二元组的问题。
def solve(arr,K):
    n=len(arr)
    for k in range(n):
        #去重，之所以只比较相邻，是因为数组已经做了排序
        if(k>0 and arr[k]==arr[k-1]):
            continue
            
        i=k+1
        j=n-1
        while i<j:
            if arr[i]+arr[j]+arr[k]==K:
    #             res.append(arr[i],arr[j])
                if arr[k]!=arr[i] and arr[k]!=arr[j] and arr[i]!=arr[j]:
                    print(arr[k],arr[i],arr[j])
                # 去重
                while i<j and arr[i]==arr[i+1]:
                    i+=1
                while i<j and arr[j]==arr[j-1]:
                    j-=1
                i+=1
                j-=1
            elif arr[i]+arr[j]+arr[k]<K:
                i+=1
            else:
                j-=1
#接收用户输入的两个整数
n,k = map(int,input().split())
#将n个整数存放到列表中
ls = list(map(int,input().split()))
solve(ls,k)