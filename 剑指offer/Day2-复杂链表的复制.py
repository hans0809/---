# 请实现 copyRandomList 函数，复制一个复杂链表。
# 在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
# 还有一个 random 指针指向链表中的任意节点或者 null。


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        # n1->n2->None to n1->n1'->n2->n2'->None
        p=head
        while p:
            Next=p.next

            p.next=Node(p.val)
            p.next.next=Next

            p=Next
        
        # 处理random指向
        p=head
        Next=head
        while p:
            Next=p.next.next

            cp=p.next# 克隆节点
            if p.random:
                cp.random=p.random.next
            else:
                cp.random=None
            
            p=Next
        
        # 拆分成两个链表，并返回克隆链表的头结点
        p=head
        cp=head.next

        cloneHead=cp# 用于返回的头结点

        while p:
            p.next=p.next.next
            p=p.next

            if cp.next:
                cp.next=cp.next.next
            else:
                cp.next=None
            cp=cp.next
        
        return cloneHead   