# 第一种写法：效率高些
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, left, right):
            import random
            pivot_idx = random.randint(left, right)
            nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= pivot:
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
        quickSort(nums, 0, len(nums)-1)        
        return nums

# 第二种写法：效率没第一种写法高
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums,left,right):
            import random
            pivot_idx = random.randint(left, right)
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
  
            pivot=right
            key=nums[pivot]
            while left < right:
                while left < right and nums[left]<=key:
                    left+=1
                while left < right and nums[right]>=key:
                    right-=1
                #到这里，nums[left]>pivot，nums[right]<pivot，所以接下来就需要交换一下这两者
                nums[left],nums[right]=nums[right],nums[left]
            nums[left],nums[pivot]=key,nums[left]#必须是交换才可以！！！！
            return left
        def quickSort(nums, left, right):
            if left >= right:
                return
            index = partition(nums, left, right)
            quickSort(nums, left, index-1)
            quickSort(nums, index+1, right)
        quickSort(nums, 0, len(nums)-1)
        return nums

