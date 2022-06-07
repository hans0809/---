# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

# 返回删除后的链表的头节点。

# 题目保证每个数字只出现一次

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummyHead=ListNode(-1)
        dummyHead.next=head

        p=head
        q=dummyHead
        while p:
            Next=p.next
            if p.val==val:
                q.next=p.next
                break
            q=p
            p=Next

        return dummyHead.next