# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

# 例如，

# [2,3,4] 的中位数是 3

# [2,3] 的中位数是 (2 + 3) / 2 = 2.5

# 设计一个支持以下两种操作的数据结构：

# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
# 示例 1：

# 输入：
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]
# 输出：[null,null,null,1.50000,null,2.00000]
# 示例 2：

# 输入：
# ["MedianFinder","addNum","findMedian","addNum","findMedian"]
# [[],[2],[],[3],[]]
# 输出：[null,null,2.00000,null,2.50000]
#  

class MedianFinder:
    #heapq默认构建小顶堆
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A=[]#小顶堆，保存较多的一半： (top)6 7 8 9 10
        self.B=[]#大顶堆，保存较少的一半：      1 2 3 4(top)

    def addNum(self, num: int) -> None:
        # 小顶堆A中元素=大顶堆B中元素+1，应该将num插入到较少的大顶堆B中
        if len(self.A)!=len(self.B):
            #但是num有可能比B中的元素大(属于A那一部分)
            heapq.heappush(self.A,num)
            heapq.heappush(self.B, -heapq.heappop(self.A))
        # 小顶堆A中元素=大顶堆B中元素，应该将num插入到较多的小顶堆A中
        else:
           #但是num可能比A中的元素小(属于B那一部分) 
           heapq.heappush(self.B,-num)
           heapq.heappush(self.A, -heapq.heappop(self.B))
    def findMedian(self) -> float:
        if len(self.A)!=len(self.B):
            return self.A[0]
        else:
            return (self.A[0]-self.B[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()