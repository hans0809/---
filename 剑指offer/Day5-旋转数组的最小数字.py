# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

# 给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。
# 例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为 1。  

# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n=len(numbers)
        left,right=0,n-1
        
        while left<right:
            mid=(left+right)//2
            # 如果从左往右是降序，那么最小值一定在mid的右侧
            if numbers[mid]>numbers[right]:
                left=mid+1
            # 如果从左往右是升序，那么最小值一定在mid左侧
            elif numbers[mid]<numbers[right]:
                right=mid
            # 如果从左往右两个相等，那么往左侧推进
            else:
                right-=1

        return numbers[left]