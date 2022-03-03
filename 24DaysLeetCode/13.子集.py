class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 排列和组合问题的答案在叶子结点，而子集问题的答案在每一个结点
        n=len(nums)
        def back_track(index):
            if len(p)<=n:
                res.append(p[:])
            for i in range(index,n):
                p.append(nums[i])
                back_track(i+1)
                p.pop()
        p=[]
        res=[]
        back_track(0)
        return res