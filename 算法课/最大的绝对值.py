# 题目：给定一个数组arr，长度为N，切一刀，分成左右两部分，左右两部分各有一个最大值，求这两个最大值的差的绝对值的最大值。
# 思路：遍历arr找到全局最大值mVal，然后mVal-min(arr[0],arr[N-1])就是答案
def maxAbs(arr):
    return max(arr)-min(arr[0],arr[len(arr)-1])
arr=[3,5,2,8,9,1,4]
print(maxAbs(arr))