class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
# 奇偶指的是位置
class Solution:
    def oddEvenList(self , head):
        # write code here
        if not head or not head.next:
            return head
        ou=head
        ji=head.next
        jiHead=ji
        while ji and ji.next:
            ou.next=ji.next
            ou=ou.next
            ji.next=ou.next
            ji=ji.next
        ou.next=jiHead
        return head