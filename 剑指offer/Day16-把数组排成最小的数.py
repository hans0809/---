# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

# 示例 1:

# 输入: [10,2]
# 输出: "102"

class Solution:
    def minNumber(self, nums: List[int]) -> str:

        # partiion:把所有小于pivot的元素放到左侧，大于pivot的元素放到右侧
        def partition(nums, left, right):
            import random
            pivot_idx = random.randint(left, right)
            nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]
            pivot = nums[left]
            while left < right:
                while left < right and nums[right]+pivot >= pivot+nums[right]:#nums[right]>=pivot
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left]+pivot <= pivot+nums[left]:#nums[left]<=pivot
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot 
            return left
        def quickSort(nums, left, right):
            if left >= right:            
                return
            index = partition(nums, left, right)   
            quickSort(nums, left, index-1)          
            quickSort(nums, index+1, right)
        
        nums=[str(num) for num in nums]
        quickSort(nums, 0, len(nums)-1)        
        return ''.join(nums)