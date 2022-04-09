class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums)==1:
            return False
        # 滑动窗口
        n = len(nums)
        s = set()
        for i in range(n):
            if i > k:
                s.remove(nums[i - k - 1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False

# 我只会写哈希
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums)==1:
            return False
        record=dict()
        for i ,num in enumerate(nums):
            if num in record and abs(i-record[num])<=k:
                return True
            else:
                record[num]=i
        return False