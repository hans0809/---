# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre=None
        p=head
        while p:
            pNext=p.next
            p.next=pre
            pre=p
            p=pNext
        return pre
            
            