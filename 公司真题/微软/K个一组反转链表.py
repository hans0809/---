# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head,tail):
            p=head
            pre=None
            while pre!=tail:
                Next=p.next

                p.next=pre
                pre=p

                p=Next
            return tail,head# tail：头结点，head：尾结点
        
        dummyHead=ListNode(-1)
        dummyHead.next=head

        pre=dummyHead

        while head:
            tail=pre

            for i in range(k):
                tail=tail.next
                if not tail:
                    return dummyHead.next
            
            Next=tail.next# 下一次要操作的子链表的头结点

            head,tail=reverse(head,tail)# 反转后的新的头结点和尾结点

            # 将反转后的链表接回原链表
            pre.next=head
            tail.next=Next

            # 为下一次做准备
            pre=tail
            head=tail.next
        
        return dummyHead.next