# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        dummyHead=ListNode(-1,head)
        q=dummyHead
        while q and q.next:
            if q.next.val==val:
                q.next=q.next.next
            else:  # 如果不加else，直接写成q=q.next，会忽略两个相邻元素值相等的情况
                q=q.next
        return dummyHead.next
                
                