def max_prefix_length(s1,s2):
    '''求解s1和s2这两个字符串的最长公共前缀的长度'''
    n1,n2=len(s1),len(s2)
    i,j=0,0 
    cnt=0
    while i<n1 and j<n2:
        if s1[i]==s2[j]:
            cnt+=1
            i+=1
            j+=1
        else:
            break
    return cnt

while True:
    try:
        n=int(input())
        strs=[]
        for i in range(n):
            cur_s=input()
            strs.append(cur_s)
        while True:
            try:
                a,b =map(int,input().split(' '))
                res=max_prefix_length(strs[a-1],strs[b-1])
                print(res)
            except:
                break
    except:
        break