# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 官方：
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next



# 我的解法
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummpHead=ListNode(-1)
        dummpHead.next=head
        p1=dummpHead#p1指向开始重复元素的前驱
        p2=dummpHead#p2遍历重复元素
        while p1.next and p1.next.next:
            if p1.next.val==p1.next.next.val:
                p2=p1.next.next
                while p2.next and p2.val==p2.next.val:
                    p2=p2.next
                p1.next=p2.next
            else:
                p1=p1.next
        return dummpHead.next
