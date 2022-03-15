
# 题目1：给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 题目2：给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
# 都直接无脑哈希表
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        record=dict()
        for num in nums:
            if num not in record:
                record[num]=1
            else:
                record[num]+=1
        for k,v in record.items():
            if v==1:
                return k