# https://www.nowcoder.com/practice/c56f6c70fb3f4849bc56e33ff2a50b6b?tpId=117&tqId=37814&rp=1&ru=/exam/oj&qru=/exam/oj&sourceUrl=%2Fexam%2Foj%3Ftab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D117%26page%3D1&difficulty=undefined&judgeStatus=undefined&tags=&title=

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addInList(self , head1, head2):
        # write code here
        stack1,stack2=[],[]
        while head1:
            stack1.append(head1.val)
            head1=head1.next
        while head2:
            stack2.append(head2.val)
            head2=head2.next
        
        head=None
        carry=0
        while stack1 or stack2 or carry:
            a=stack1.pop() if stack1 else 0
            b=stack2.pop() if stack2 else 0
            t=a+b+carry
            carry=t//10# 进位
            newNode=ListNode(t%10)
            newNode.next=head
            head=newNode
        return head