# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead=ListNode(-1)
        p=dummyHead
        p1,p2=list1,list2
        while p1 and p2:
            if p1.val<p2.val:
                p.next=p1
                p1=p1.next
            else:
                p.next=p2
                p2=p2.next
            p=p.next
        while p1:
            p.next=p1
            p=p.next
            p1=p1.next
        while p2:
            p.next=p2
            p=p.next
            p2=p2.next
        return dummyHead.next
