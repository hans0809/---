# 和14题几乎一样的代码
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummyHead=ListNode(-1,head)
        p=dummyHead
        while p.next and p.next.next:
            if p.next.val==p.next.next.val:
                x=p.next.val
                p=p.next
                while p.next and p.next.val==x:
                        p.next=p.next.next
            else:
                p=p.next
        return dummyHead.next


# 简单写法
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummyHead=ListNode(-1,head)
        p=head
        while p.next:
            if p.val==p.next.val:
                p.next=p.next.next
            else:
                p=p.next
        return dummyHead.next