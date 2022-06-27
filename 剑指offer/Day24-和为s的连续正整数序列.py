# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

# 示例 1：

# 输入：target = 9
# 输出：[[2,3,4],[4,5]]
# 示例 2：

# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]



# 算法流程：
# 初始化： 左边界i=1 ，右边界 j=2 ，元素和 s = 3 ，结果列表 res ；

# 循环： 当 i≥j 时跳出；

# 当 s > target 时： 向右移动左边界 i = i + 1 ，并更新元素和 s ；
# 当 s < target 时： 向右移动右边界 j = j + 1 ，并更新元素和 s ；
# 当 s = target 时： 记录连续整数序列，并向右移动左边界 i = i + 1；
# 返回值： 返回结果列表 res ；

# 滑动窗口
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i,j=1,2
        s=3
        res=[]
        while i<j:
            if s==target:
                res.append(list(range(i,j+1)))
            if s>=target:
                s-=i
                i+=1
            elif s<target:
                j+=1
                s+=j
        return res