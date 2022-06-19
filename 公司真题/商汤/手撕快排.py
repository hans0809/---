#第二种写法好记一些

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n<=1:
            return nums
        
        def partition(arr,L,R):
            if L>=R:
                return 
            
            pivot=arr[R]#pivot
            s=L-1#s是小于num区域的右边界
            b=R#b是大于num区域的左边界
            p=L#遍历nums中的每个元素

            while p<b:
                if arr[p]==pivot:
                    p+=1
                elif arr[p]<pivot:
                    arr[s+1],arr[p]=arr[p],arr[s+1]
                    s+=1
                    p+=1
                elif arr[p]>pivot:
                    arr[p],arr[b-1]=arr[b-1],arr[p]
                    b-=1
            # 此时，左侧区域全部小于num，中间区域全部等于num，
            # 右侧区域除了最后一个(arr[R])外，都大于num
            # 因此，只需将右侧区域最后一个元素arr[R]与右侧区域第一个元素(左侧边界)交换，就完成了
            arr[b],arr[R]=arr[R],arr[b]
            # 此时，大于num区域的左边界不再是b，而是b+1

            # 返回等于num=arr[R]区域的左右边界，这个范围内的元素都等于arr[R]，
            # 并且都已经来到了排序后的最终位置了，之后无需再动
            return [s+1,b]


        def process(arr,L,R):
            if L>=R:
                return 

            # 随机找一个元素与arr[R]做交换
            import random
            index=random.choice(list(range(L,R)))# index in {L,L+1,L+2,...,R-2,R-1}
            arr[R],arr[index]=arr[index],arr[R]

            a,b=partition(arr,L,R)
            process(arr,L,a-1)
            process(arr,b+1,R)

        process(nums,0,n-1)
        return nums


# 另外一种简便写法
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(arr, low, high):
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
        

        def quickSort(arr, low, high):
            if low >= high:             # 递归结束
                return  
            mid = partition(arr, low, high)     # 以mid为分割点，右边元素>左边元素
            quickSort(arr, low, mid-1)          # 递归对mid两侧元素进行排序
            quickSort(arr, mid+1, high)
        

        quickSort(nums, 0, len(nums)-1)         # 调用快排函数对nums进行排序
        return nums