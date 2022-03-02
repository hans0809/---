class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找
        n=len(nums)
        left=0
        right=n
        while left<right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[0]<=nums[mid]:#[left,mid]是有序数组
                if nums[mid]>target>=nums[0]:# >=nums[0]保证target存在
                    right=mid
                else:
                    left=mid+1
            elif nums[0]>nums[mid]:#[mid,right]是有序数组
                if nums[mid]<target<=nums[n-1]:#<=nums[n-1]保证target存在
                    left=mid+1
                else:
                    right=mid
        return -1

# 扩展：上面这题是求旋转数组中的target所在下标，下面这题是求旋转数组中的最小值
#https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=295&tqId=23269&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Ftab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295
class Solution:
    def minNumberInRotateArray(self , rotateArray: List[int]) -> int:
        # write code here
        n=len(rotateArray)
        l,r=0,n-1
        while l<r:
            mid=(l+r)//2
            if rotateArray[mid]>rotateArray[r]:# jiangxu
                l=mid+1
            elif rotateArray[mid]==rotateArray[r]:
                r=r-1
            else:
                r=mid
        return rotateArray[l]