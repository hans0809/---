# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or  not head.next or k==0:
            return head

        p=head
        n=0# 链表长度
        while p:
            n+=1
            p=p.next

        k=k%n
        if k==0:
            return head

        p=head
        for i in range(n-k-1):
            p=p.next
        
        part2_head=p.next
        p.next=None

        q=part2_head
        while q.next:
            q=q.next
        
        q.next=head

        return part2_head