# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1=l1
        p2=l2
        dummyHead=ListNode(-1)
        p=dummyHead

        while p1 and p2:
            if p1.val<p2.val:
                p.next=p1
                p1=p1.next
            else:
                p.next=p2
                p2=p2.next
            p=p.next
        
        if p1:
            p.next=p1
        if p2:
            p.next=p2
        
        return dummyHead.next