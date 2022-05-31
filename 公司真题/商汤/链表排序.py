# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 链表的插入排序O(N^2)
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummyHead=ListNode(-1)
        dummyHead.next=head

        lastSorted=head# 有序链表的末尾结点

        cur=head.next
        
        while cur:
            if lastSorted.val<=cur.val:
                lastSorted=lastSorted.next
            else:
                pre=dummyHead
                while pre.next.val<=cur.val:
                        pre=pre.next
                # 此时pre来到第一个>=cur.val的前驱位置
                lastSorted.next=cur.next# 下一个待插入的元素
                cur.next=pre.next
                pre.next=cur

            cur=lastSorted.next# 下一次，cur来指向下一个待插入的元素

        return dummyHead.next

# 链表的归并排序O(NlogN)

# 方法一：自顶向下归并排序，空间复杂度为O(N)
# 对链表自顶向下归并排序的过程如下。

# 找到链表的中点，以中点为分界，将链表拆分成两个子链表。寻找链表的中点可以使用快慢指针的做法，快指针每次移动 22 步，慢指针每次移动 11 步，当快指针到达链表末尾时，慢指针指向的链表节点即为链表的中点。

# 对两个子链表分别排序。

# 将两个排序后的子链表合并，得到完整的排序后的链表。可以使用「21. 合并两个有序链表」的做法，将两个有序的子链表进行合并。

# 上述过程可以通过递归实现。递归的终止条件是链表的节点个数小于或等于 1，即当链表为空或者链表只包含 1 个节点时，不需要对链表进行拆分和排序。
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # 寻找链表中点
        def find_seq_lst_middle(head,tail):
            slow,fast=head,head
            # while fast and fast.next:
            #     slow=slow.next
            #     fast=fast.next.next
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            return slow
        # 合并两个有序链表
        def merge_two_seq_lst(head1,head2):
            dummyHead=ListNode(-1)
            p=dummyHead

            p1,p2=head1,head2
            while p1 and p2:
                if p1.val<p2.val:
                    p.next=p1
                    p1=p1.next
                else:
                    p.next=p2
                    p2=p2.next

                p=p.next
            
            if p1:
                p.next=p1
            else:
                p.next=p2

            return dummyHead.next

        # 链表归并排序入口
        def sortFunc(head,tail):
            if not head:
                return head
            if head.next == tail:
                head.next=None
                return head

            mid_node=find_seq_lst_middle(head,tail)# 子链表的中间结点，所以返回的是head到tail这一段子链表的中间结点
            return merge_two_seq_lst(sortFunc(head,mid_node),sortFunc(mid_node,tail))
        
        return sortFunc(head,None)








