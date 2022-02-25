# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead=ListNode(-1)
        dummyHead.next=head
        
        p1=dummyHead
        p2=dummyHead
        
        for i in range(n):
            p2=p2.next
        
        while p2.next:
            p1=p1.next
            p2=p2.next
            
        # 此时p1来到待删除结点的前面
        p1.next=p1.next.next
        return dummyHead.next
            