# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

#  

# 示例 1：

# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 示例 2：

# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9

#先排序，O(NlogN)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=1:
            return n

        nums.sort()

        maxCnt=-1#答案
        cnt=1#计数器
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                if i==1:
                    maxCnt=max(maxCnt, cnt)#处理类似[0, 0]的数据
                continue
            elif nums[i]==nums[i-1]+1:
                cnt+=1
            else:
                cnt=1
            
            maxCnt=max(maxCnt, cnt)
        return maxCnt


# 空间换时间,来自官方题解
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak