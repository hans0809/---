# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

# 返回 s 所有可能的分割方案。

# 示例: 输入: "aab" 输出: [ ["aa","b"], ["a","a","b"] ]


# 思路：类似组合问题

# 例如对于字符串abcdef：

# 组合问题：选取一个a之后，在bcdef中再去选取第二个，选取b之后在cdef中在选组第三个.....。
# 切割问题：切割一个a之后，在bcdef中再去切割第二段，切割b之后在cdef中在切割第三段.....。

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        res=[]
        path=[]

        def backtrack(s,start_index):
            if start_index>n-1:
                res.append(path[:])
                return
            
            for i in range(start_index,n):# i相当于切割点
                # 判断s[start_index...i]是否是回文串
                tmp=s[start_index:i+1]
                if tmp==tmp[::-1]:
                    path.append(tmp)
                    backtrack(s,i+1)
                    path.pop()
                else:
                    continue
        backtrack(s,0)
        return res