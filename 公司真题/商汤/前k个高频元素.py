# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rec=dict()
        for num in nums:
            if num in rec:
                rec[num]+=1
            else:
                rec[num]=1
        print(rec)
        # 小顶堆，长度为k，满了就把小的移出，最后只剩下k个比较大的，就是答案
        queue=[]
        for num,frec in rec.items():
            heapq.heappush(queue,(frec,num))
            if len(queue)>k:
                heapq.heappop(queue)
        print(queue)
        return [heapq.heappop(queue)[1] for _ in range(k)]       