# 输入两个链表，找出它们的第一个公共节点。

# 思路：我走过你走过的路，这样我们算不算相拥~

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1=headA
        p2=headB

        while p1!=p2:
            p1=p1.next if p1 else headB
            p2=p2.next if p2 else headA
        
        return p1