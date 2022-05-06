# 小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。

# 如果小镇法官真的存在，那么：

# 小镇法官不会信任任何人。
# 每个人（除了小镇法官）都信任这位小镇法官。
# 只有一个人同时满足属性 1 和属性 2 。
# 给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。

# 如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。

# 思路：
# 统计每个人信任别人的数量和被信任的数量，
# 如果存在某个人信任别人的数量为0，且被信任的数量为 n-1，那么，这个人就是法官。

# 我写的
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        rec=dict()#统计每个人信任其余人的数量
        rec2=dict()#统计每个人被别人信任的数量
        for item in trust:
            k,v=item[0],item[1]#k信任v

            if k not in rec:
                rec[k]=1
            else:
                rec[k]+=1
            
            if v not in rec2:
                rec2[v]=1
            else:
                rec2[v]+=1
            
        for i in range(1,n+1):
            if rec.get(i,0)==0 and rec2.get(i,0)==n-1:
                return i
        
        return -1

# 我写的用数组代替哈希表，貌似这样更简洁些
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        rec=[[0 for _ in range(2)] for _ in range(n+1)]#(n+1)x2
        #rec[i][0]:编号为i的信任其他人的数量
        #rec[i][1]:编号为i的人被他人信任的数量
        # i=1,2,...,n

        for item in trust:
            k,v=item[0],item[1]#k信任v
            rec[k][0]+=1
            rec[v][1]+=1
        
        for i in range(1,n+1):
            if rec[i][0]==0 and rec[i][1]==n-1:
                return i
        
        return -1