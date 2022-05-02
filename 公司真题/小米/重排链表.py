# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：

# L0 → L1 → … → Ln - 1 → Ln
# 请将其重新排列后变为：

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return 

        # 找寻中间节点
        slow=head
        fast=head
        pre=head#中间节点的前驱节点
        while fast and fast.next:
            pre=slow
            slow=slow.next
            fast=fast.next.next
        # 此时slow就是链表的中间节点
        # print(slow.val)
        pre.next=None#slow的前驱后面截断，链表分成两段

        # 把slow及其之后的链表段反转
        def reverse_linklist(head):
            p=head
            pre=None
            while p:
                NEXT=p.next

                p.next=pre
                pre=p

                p=NEXT
            return pre
        rev_lst=reverse_linklist(slow)
        # print(rev_lst)

        # 将head和rev_lst 合并
        p=ListNode(-1)
        p1=head
        p2=rev_lst
        # print(p1,p2)

        while p1 and p2:
            p1_next=p1.next
            p2_next=p2.next
            
            p.next=p1
            p=p.next
            p.next=p2
            p=p.next

            p1=p1_next
            p2=p2_next
        while p1:
            p1_next=p1.next
            p.next=p1
            p=p.next
            p1=p1.next
        while p2:
            p2_next=p2.next
            p.next=p2
            p=p.next
            p2=p2_next