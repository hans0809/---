# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
            
        # 找到倒数第k%n个结点，将这个结点及其后面的结点弄到链表前面
        n=0# 链表长度
        p=head
        while p:
            n+=1
            p=p.next
        step=k%n
        if step==0:
            return head
        # 接下来，找到倒数第step个结点及其前驱，断开它们，并将后面一段弄到链表前面去
        p=head
        for i in range(n-step-1):
            p=p.next
        # 此时p来到了倒数第step个结点的前驱
        partHead=p.next# 后一段的头节点
        p.next=None# 切开成两段
        
        partTail=None#后一段的尾节点
        ph=partHead
        while ph:
            partTail=ph
            ph=ph.next
        partTail.next=head
        return partHead
        
        
        
        