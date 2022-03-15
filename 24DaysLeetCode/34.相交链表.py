# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法1：双指针
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p1=headA
        p2=headB
        len1=len2=0
        while p1:
            len1+=1
            p1=p1.next
        while p2:
            len2+=1
            p2=p2.next
        if p1!=p2:
            return None
        # p1遍历长的，p2遍历短的
        if len1>len2:
            p1=headA
            p2=headB
        else:
            p1=headB
            p2=headA
        # 快的先走gap步
        gap=abs(len1-len2)
        for _ in range(gap):
            p1=p1.next
        # 接下来一起走，第一次相遇的结点就是相交的起始结点
        while p1 != p2:
            p1=p1.next
            p2=p2.next
        return p1

#方法2：哈希
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p1=headA
        p2=headB
        record=set()
        while p1:
            record.add(p1)
            p1=p1.next
        while p2:
            if p2 in record:
                return p2
            p2=p2.next
        return None
        