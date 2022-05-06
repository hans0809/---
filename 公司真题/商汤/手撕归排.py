class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n<=1:
            return nums
            
        def merge(nums,L,mid,R):
            #将[L,mid]和[mid+1,R]这两段分别有序但整体无序的数组 合并成一段有序数组
            res=[]
            p1,p2=L,mid+1
            while p1<=mid and p2<=R:
                if nums[p1]<=nums[p2]:
                    res.append(nums[p1])
                    p1+=1
                else:
                    res.append(nums[p2])
                    p2+=1
            while p1<=mid:
                res.append(nums[p1])
                p1+=1
            while p2<=R:
                res.append(nums[p2])
                p2+=1
            
            nums[L:(L+len(res))]=res
        def process(nums,L,R):
            if L==R:
                return 
            mid=(L+R)//2
            process(nums,L,mid)# 对左半部分进行排序
            process(nums,mid+1,R)# 对右半部分进行排序

            # 每次process要做的事就是把两段 `分别有序但整体无序的数组` 合并成`一段有序数组`
            merge(nums,L,mid,R)

        process(nums,0,n-1)
        return nums