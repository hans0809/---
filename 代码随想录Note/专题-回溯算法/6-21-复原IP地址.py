# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

# 有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

# 示例 1：

# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 示例 2：

# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 示例 3：

# 输入：s = "1111"
# 输出：["1.1.1.1"]
# 示例 4：

# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]


# 思路：类似切割问题
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n=len(s)
        res=[]
        path=[]

        def is_valid(sub_s):
            start,end=0,len(sub_s)-1
            if sub_s[start]=='0' and start!=end:
                return False
            if not 0<=int(sub_s)<=255:
                return False
            
            return True

        def backtrack(s,start_index):
            if len(path)==4:
                if start_index>n-1:
                    res.append('.'.join(path[:]))
                    # return
                return# 放这儿能加速，因为一旦已经切分了3次(len(path)==4)，那么不管最后一段合不合法，都要结束了
                # 合法就是切分点正好位于最后一个元素位置，不合法就是切分点后面还有数字
            
            for i in range(start_index,n):# i相当于切割点,start_index 是开始切割的地方，前面不用管
                tmp=s[start_index:i+1]
                if is_valid(tmp):
                    path.append(tmp)
                    backtrack(s,i+1)#i+1 !!! 
                    path.pop()
                else:
                    break
        
        backtrack(s,0)

        return res