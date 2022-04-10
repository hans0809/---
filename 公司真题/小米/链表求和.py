# 给定两个用链表表示的整数，每个节点包含一个数位。

# 这些数位是反向存放的，也就是个位排在链表首部。

# 编写函数对这两个整数求和，并用链表形式返回结果。


# 示例：

# 输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
# 输出：2 -> 1 -> 9，即912


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans=ListNode(-1)
        p=ans
        carry=0
        p1,p2=l1,l2
        while p1 and p2:
            carry, num=(carry+p1.val+p2.val)//10, (carry+p1.val+p2.val)%10
            ans.next=ListNode(num)
            ans=ans.next
            p1=p1.next
            p2=p2.next
        while p1:
            carry,num=(p1.val+carry)//10,(p1.val+carry)%10
            ans.next=ListNode(num)
            ans=ans.next
            p1=p1.next
        while p2:
            carry,num=(p2.val+carry)//10,(p2.val+carry)%10
            ans.next=ListNode(num)
            ans=ans.next
            p2=p2.next
        if carry!=0:
            ans.next=ListNode(carry)
            ans=ans.next
        return p.next