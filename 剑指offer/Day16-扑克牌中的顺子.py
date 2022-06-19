# 从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。
# A 不能视为 14。

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        n=len(nums)#n=5
        joker=0# 大小王的数量
        nums.sort()
        for i in range(n-1):#i=0,1,2,3
            if nums[i]==0:
                joker+=1
            elif nums[i]==nums[i+1]:
                return False
        return nums[n-1]-nums[joker]<5#最大值与最小值(不包括0)之差小于5就是顺子
            