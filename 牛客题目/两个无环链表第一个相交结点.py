
# 解法1：长的先走几步，然后同步走
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        def calLen(p):
            res=0
            while p:
                p=p.next
                res+=1
            return res
        len1=calLen(pHead1)
        len2=calLen(pHead2)
        def walkStep(p,step):
            while step:
                p=p.next
                step-=1
            return p
        # 长的先走几步
        if len1>len2:
            pHead1=walkStep(pHead1, len1-len2)
        else:
            pHead2=walkStep(pHead2, len2-len1)
        # 此时两个指针后面部分长度一样】
        while pHead1!=pHead2:
            pHead1=pHead1.next
            pHead2=pHead2.next
            if not pHead1:
                return None
        return pHead1
#         #这两种写法等价
#         while pHead1:
#             if pHead1==pHead2:
#                 return pHead1
#             pHead1=pHead1.next
#             pHead2=pHead2.next
#         return None


# 解法2：哈希，笔试用
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
       #方法2：哈希
        p1,p2=pHead1,pHead2
        record=set()
        while p1:
            record.add(p1)
            p1=p1.next
        while p2:
            if p2 in record:
                return p2
            p2=p2.next
        return None