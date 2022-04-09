# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

# 示例 1:
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]

# 示例 2:
# 输入: nums = [1], k = 1
# 输出: [1]


# 我直接。。。
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record=dict()
        for i in nums:
            if i  in record:
                record[i]+=1
            else:
                record[i]=0
        record=sorted(record.items(),key=lambda x:x[1])[::-1]
        return [k for k,v in record ][:k]


# 使用堆结构维护一个长度为k的优先队列，使用小顶堆，这样最后队列中保留的就是前k个大的元素了
class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record=dict()
        for i in nums:
            if i  in record:
                record[i]+=1
            else:
                record[i]=0
        
        # 小顶堆构建优先队列
        priority_queue=[]

        for key,freq in record.items():
            heapq.heappush(priority_queue,(freq,key))
            if len(priority_queue)>k:
                heapq.heappop(priority_queue)
        
        result=[0]*k
        for i in range(k-1,-1,-1):
            result[i]=heapq.heappop(priority_queue)[1]
        
        return result

