# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead=ListNode(-1)
        p=dummyHead
        p1=list1
        p2=list2
        while p1 and p2:
            if p1.val<p2.val:
                p.next=p1
                p=p1
                p1=p1.next
            else:
                p.next=p2
                p=p2
                p2=p2.next
        while p1:
            p.next=p1
            p=p.next
            p1=p1.next
        while p2:
            p.next=p2
            p=p.next
            p2=p2.next
        # 上面这两个while等价于下面这一句
        #p.next=p1 if p1 else p2
        return dummyHead.next