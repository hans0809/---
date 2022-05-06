# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummyHead=ListNode(-100000000000,head)
        p=dummyHead#遍历
        q=head#指向某一个重复数字的最后一个重复位置的后面

        while p:
            while q and q.val==p.val:
                q=q.next
            #此时q来到第一个不等于p的val的节点
            p.next=q
            p=q
        return dummyHead.next

# 加难度：给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummyHead=ListNode(-100000000000,head)
        pre=dummyHead#指向开始重复元素的前一个位置
        p=head

        while p and p.next:
            if p.val==p.next.val:
                tmp=p.val
                while p and p.val==tmp:
                    p=p.next
                pre.next=p
            else:
                pre=p
                p=p.next
        return dummyHead.next