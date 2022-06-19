# 输入整数数组 arr ，找出其中最小的 k 个数。
# 例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

# 借鉴top-k的写法
class Solution:
    def getLeastNumbers(self, nums: List[int], k: int) -> List[int]:
        def topk_split(nums,  left, right):
            #寻找到第k个数停止递归，使得nums数组中index左边是前k个小的数，index右边是后面n-k个大的数
            if left>=right:
                return
            index = partition(nums, left, right)
            print(index)
            if index==k:
                print('找到',index)
                return
            elif index < k:
                topk_split(nums, index+1, right)
            else:
                topk_split(nums, left, index-1)
        def partition( arr, low, high):
            import random
            pivot_idx = random.randint(low, high)                   # 随机选择pivot
            arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]     # pivot放置到最左边
            pivot = arr[low]                                        # 选取最左边为pivot

            left, right = low, high     # 双指针
            while left < right:
                
                while left<right and arr[right] >= pivot:          # 找到右边第一个<pivot的元素
                    right -= 1
                arr[left] = arr[right]                             # 并将其移动到left处
                
                while left<right and arr[left] <= pivot:           # 找到左边第一个>pivot的元素
                    left += 1
                arr[right] = arr[left]                             # 并将其移动到right处
            
            arr[left] = pivot           # pivot放置到中间left=right处
            return left
     
        left,right=0,len(nums)-1
        topk_split(nums,left,right)
        return nums[:k]


# 我写的
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def partition(arr,left,right):
            import random
            pivot_index=random.randint(left,right)
            arr[left],arr[pivot_index]=arr[pivot_index],arr[left]
            pivot=arr[left]

            while left<right:
                while left<right and arr[right]>=pivot:
                    right-=1
                arr[left]=arr[right]
                while left<right and arr[left]<=pivot:
                    left+=1
                arr[right]=arr[left]

                arr[left]=pivot
            
            return left
        
        def get_min_k(arr,left,right):
            if left>=right:
                return

            index=partition(arr,left,right)
            if index==k:
                return 
            elif index<k:
                get_min_k(arr,index+1,right)
            elif index>k:
                get_min_k(arr,left,index-1)
        
        n=len(arr)
        get_min_k(arr,0,n-1)
        print(arr)
        return arr[:k]