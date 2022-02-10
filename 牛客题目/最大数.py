# 给定一个长度为n的数组nums，数组由一些非负整数组成，现需要将他们进行排列并拼接，
# 每个数不可拆分，使得最后的结果最大，返回值需要是string类型，否则可能会溢出。
class Solution:
    def solve(self , nums):
        # write code here
        def compare(a,b):
            return int(a)<int(b)
        # 冒泡排序
        n=len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                a=nums[j]
                b=nums[j+1]
                sum1=str(a)+str(b)
                sum2=str(b)+str(a)
                # 如果sum1<sum2,那么b应该在a前面
                if compare(sum1,sum2):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        if nums[0]==0:
            return '0'
        return ''.join(str(i) for i in nums) 