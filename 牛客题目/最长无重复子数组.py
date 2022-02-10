# 给定一个长度为n的数组arr，返回arr的最长无重复元素子数组的长度，无重复指的是所有数字都不相同。
# 子数组是连续的，比如[1,3,5,7,9]的子数组有[1,3]，[3,5,7]等等，但是[1,3,7]不是子数组
# https://www.nowcoder.com/practice/b56799ebfd684fb394bd315e89324fb4?tpId=117&tqId=37816&rp=1&ru=/exam/oj&qru=/exam/oj&sourceUrl=%2Fexam%2Foj%3Ftab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D117%26page%3D1&difficulty=undefined&judgeStatus=undefined&tags=&title=
class Solution:
    def maxLength(self , arr):
        # write code here
        n=len(arr)
        s=set()
        s.add(arr[0])
        i=0
        j=1
        res=1
        while j<n:
            if arr[j] not in s:
                s.add(arr[j])
                j+=1
            else:
                s.remove(arr[i])
                i+=1
            res=max(res,len(s))
        return res
class Solution:
    def maxLength(self , arr):
        # write code here
        n=len(arr)
        if n<2:
            return n
        s=dict()
        i=0
        j=0
        res=0
        while j<n:
            if arr[j] not in s:
                s[arr[j]]=j
#                 j+=1
            else:
                i=max(i,s[arr[j]]+1)
                s[arr[j]]=j
#                 j+=1
            res=max(res,j-i+1)
            j+=1
        return res