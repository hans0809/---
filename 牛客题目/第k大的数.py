# 有一个整数数组，请你根据快速排序的思路，找出数组中第 k 大的数。

class Solution:
    def findKth(self , nums, n,  k):
        # write code here
        left,right=0,len(nums)-1

        #self.quicksort(nums,left,right)
        self.topk_split(nums,len(nums)-k,left,right)

        return nums[len(nums)-k]
        # 例子：1 2 3 4 5 K=2
    def partition(self,arr,L,R):
        if L>=R:
            return 
        num=arr[R]#枢纽
        s=L-1#指向小于等于num区域(也就是左边区域)的右边界
        p=L#遍历用的指针
        while p<R:#下标为R的元素是num，先不动它
            if arr[p]<=num:
                arr[s+1],arr[p]=arr[p],arr[s+1]
                s+=1
                p+=1
            else:
                p+=1
        #此时小于等于区域的右边界是s，s+1位置是大于num的区域的左边界
        #将arr[R]与大于num区域的左边界(下标为s+1)进行交换
        arr[s+1],arr[R]=arr[R],arr[s+1]
        #于是小于等于区域的右边界变成s+1
        #s+1位置就是元素arr[R]最终排序后的位置，之后它就不用动了
        return s+1

    #普通快排，这里用不到 ，只是回顾一下
    def quicksort(self,nums, left, right):
        if left < right:
            index = self.partition(nums, left, right)
            self.quicksort(nums, left, index-1)
            self.quicksort(nums, index+1, right)

    #改编自quicksort
    def topk_split(self,nums, k, left, right):
        #寻找到第k个数停止递归，使得nums数组中index左边是前k个小的数，index右边是后面n-k个大的数
        if (left<right):
            index = self.partition(nums, left, right)
            print(index)
            if index==k:
                print('找到',index)
                return 
            elif index < k:
                self.topk_split(nums, k, index+1, right)
            else:
                self.topk_split(nums, k, left, index-1)

# 另一种partition写法
class Solution:
    def findKth(self , nums, n, k):
        # write code here
        left,right=0,len(nums)-1
 
        #self.quicksort(nums,left,right)
        self.topk_split(nums,len(nums)-k,left,right)
        # 求第k大的数，相当于求求len(nums)-k个小的数
 
        return nums[len(nums)-k]
    def partition(self,nums,left,right):
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
     
    #普通快排，这里用不到 ，只是回顾一下
    def quicksort(self,nums, left, right):
        if left < right:
            index = self.partition(nums, left, right)
            self.quicksort(nums, left, index-1)
            self.quicksort(nums, index+1, right)
 
    #改编自quicksort
    def topk_split(self,nums, k, left, right):
        #寻找到第k个数停止递归，使得nums数组中index左边是前k个小的数，index右边是后面n-k个大的数
        if (left<right):
            index = self.partition(nums, left, right)
            print(index)
            if index==k:
                print('找到',index)
                return
            elif index < k:
                self.topk_split(nums, k, index+1, right)
            else:
                self.topk_split(nums, k, left, index-1)