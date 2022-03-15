# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 寻找链表中点(奇数：中点；偶数：上中点)
        def find_mid(head):
            slow=head
            fast=head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            #此时slow就是奇数时的中间结点，偶数时的上中点
            return slow
        #合并两个链表，使其有序
        def mergeTwoLinkList(link1,link2):
            dummyHead=ListNode(-1)
            p=dummyHead
            while link1 and link2:
                if link1.val<link2.val:
                    link1Next=link1.next
                    p.next=link1
                    link1=link1Next
                else:
                    link2Next=link2.next
                    p.next=link2
                    link2=link2Next
                p=p.next
            if link1:
                p.next=link1
            if link2:
                p.next=link2
            return dummyHead.next
        # 主函数入口
        def mergeSortLinkList(head):
            if not head or not head.next:
                return head
            left_end=find_mid(head)
            mid=left_end.next
            # 切开
            left_end.next=None
            
            # 递归
            left=mergeSortLinkList(head)
            right=mergeSortLinkList(mid)
            
            return mergeTwoLinkList(left,right)
        return mergeSortLinkList(head)

# 也可以查找链表的上中点(奇数：上中点；偶数：上中点)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 寻找链表中点(奇数：中点；偶数：上中点)
        def find_mid(head):
            slow=head
            fast=head.next
            while fast.next and fast.next.next:
                slow=slow.next#慢指针每次走一步
                fast=fast.next.next#快指针每次走两步
                
            return slow
        #合并两个链表，使其有序
        def mergeTwoLinkList(link1,link2):
            dummyHead=ListNode(-1)
            p=dummyHead
            while link1 and link2:
                if link1.val<link2.val:
                    link1Next=link1.next
                    p.next=link1
                    link1=link1Next
                else:
                    link2Next=link2.next
                    p.next=link2
                    link2=link2Next
                p=p.next
            if link1:
                p.next=link1
            if link2:
                p.next=link2
            return dummyHead.next
        # 主函数入口
        def mergeSortLinkList(head):
            if not head or not head.next:
                return head
            left_end=find_mid(head)
            mid=left_end.next
            # 切开
            left_end.next=None
            
            # 递归
            left=mergeSortLinkList(head)
            right=mergeSortLinkList(mid)
            
            return mergeTwoLinkList(left,right)
        return mergeSortLinkList(head)