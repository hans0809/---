# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre=None
        p=head
        while p:
            next=p.next

            p.next=pre
            pre=p
            
            p=next
        
        return pre