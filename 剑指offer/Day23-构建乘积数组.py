# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
# 其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积,
# 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n=len(a)
        if n==0:
            return []

        left=[0 for _ in range(n)]# left[i]代表a[0...i-1]所有元素的乘积
        p=1
        for i in range(n):
            p*=a[i]
            left[i]=p
        
        right=[0 for _ in range(n)]# right[i]代表a[i...n-1]所有元素的乘积
        p=1
        for i in range(n-1,-1,-1):
            p*=a[i]
            right[i]=p
        
        b=[0 for _ in range(n)]
        b[0]=right[1]
        b[n-1]=left[n-2]
        for i in range(1,n-1):
            b[i]=left[i-1]*right[i+1]
        
        return b