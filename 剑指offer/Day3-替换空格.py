# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

# 空间复杂度为O（N），在别的语言能够达到O（1）,这是因为Python的string类型是不可变的，所以用了一个list
class Solution:
    def replaceSpace(self, s: str) -> str:
        if not s:
            return ''

        s=list(s)
        n=len(s)# 原字符串长度
        num_spaces=s.count(' ')# 原字符串空格数量

        res=copy.deepcopy(s)
        res.extend([' ']*2*num_spaces)# 替换后的字符串
        n_res=len(res)# 替换后字符串的长度

        p1,p2=n-1,n_res-1# 设置双指针

        while p1>=0:
            if s[p1]!=' ':
                res[p2]=s[p1]
                p2-=1
            else:
                res[p2-2:p2+1]='%20'
                p2-=3
            p1-=1
        
        return ''.join(res) 