# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        record=dict()
        for num in nums:
            if num not in record:
                record[num]=1
            else:
                record[num]+=1
            
            if record[num]>n//2:
                return num