# 求取一个数组最大K个数，返回K个数结果为有序数组。假设数组有N个元素，要求算法时间复杂度不超过O(N*log(K))，空间复杂度为O（1）。
# 如：
# input：
# [3, 2, 1, 4, 5]
# 2
# output：
# [4, 5]


# 输入描述:
# 输入一个包含N个元素的数组和数量K

# 输出描述:
# 输出最大的K个数，返回结果为一个有序的递增数组

# 输入例子1:
# [3,2,1,4,5]
# 2

# 输出例子1:
# [4, 5]

def run(nums,k):
    # 构建一个小顶堆，大小为k，每次堆满后，优先弹出小的元素，因此最后保留下来的就是前k大的元素了
    queue=[]
    import heapq
    for num in nums:
        heapq.heappush(queue,num)
        if len(queue)>k:
            heapq.heappop(queue)
    
    res=[heapq.heappop(queue) for _ in range(k)]
    return res

while True:
    try:
        nums=eval(input())
        k=int(input())
        res=run(nums,k)
        print(res)
    except:
        break