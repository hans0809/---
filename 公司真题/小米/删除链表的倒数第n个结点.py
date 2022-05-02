# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead=ListNode(-1,head)
        p=dummyHead
        q=dummyHead
        pre=p#q的前驱
        for i in range(n):
            p=p.next

        while p:
            p=p.next
            pre=q
            q=q.next
        
        pre.next=pre.next.next

        return dummyHead.next