# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummyHead=ListNode(-1,head)
        lastSorted=head
        cur=head.next
        while cur:
            if lastSorted.val<=cur.val:
                lastSorted=lastSorted.next
            else:
                prev=dummyHead
                while prev.next.val<cur.val:
                    prev=prev.next
                #prev来到cur最终位置的前驱
                lastSorted.next=cur.next
                cur.next=prev.next
                prev.next=cur
            cur=lastSorted.next

        return dummyHead.next
            
            