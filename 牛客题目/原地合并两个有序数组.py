# 给出一个有序的整数数组 A 和有序的整数数组 B ，请将数组 B 合并到数组 A 中，变成一个有序的升序数组
# 注意：
# 1.保证 A 数组有足够的空间存放 B 数组的元素， A 和 B 中初始的元素数目分别为 m 和 n，A的数组空间大小为 m+n
# 2.不要返回合并的数组，将数组 B 的数据合并到 A 里面就好了
# 3. A 数组在[0,m-1]的范围也是有序的

# 思路：从后往前依次填充，避免覆盖A中原来的元素
class Solution:
    def merge(self , A, m, B, n):
        # write code here
        i=m-1#遍历A
        j=n-1# 遍历B
        tail=m+n-1# 从后往前填充
        while i>=0 and j>=0:
            if A[i]>B[j]:
                A[tail]=A[i]
                i-=1
            else:
                A[tail]=B[j]
                j-=1
            tail-=1
        while i>=0:
            A[tail]=A[i]
            i-=1
            tail-=1
        while j>=0:
            A[tail]=B[j]
            j-=1
            tail-=1