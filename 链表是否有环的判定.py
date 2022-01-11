#题目：判断一个链表中是否有环，如果有，请给出入环节点

#################首先创建单链表###########################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
n=6
nodes=[ListNode(i) for i in range(1,n)]

head=ListNode(0)
p=head
for i in range(n-1):
    p.next=nodes[i]
    p=nodes[i]
p.next=nodes[1]#设置为有环链表

#链表：0->1->2->3->4->5->2->None

#####################笔试解法：哈希set###########################

def has_circle1(head):
    if not head or not head.next or not head.next.next:#空或者单节点或者只有两个节点
        print("无环")
        return
    hashset=set()
    p=head
    while p:
        print(p.val,end='->')
        if p in hashset:
            print("有环，入环节点是：",p.val)
            return p
        hashset.add(p)
        p=p.next
    print("无环")
    return
has_circle1(head)

#####################面试解法：快慢指针###########################

def has_circle2(head):
    if not head or not head.next or not head.next.next:#空或者单节点或者只有两个节点
        print("无环")
        return

    slow=head.next
    fast=head.next.next

    while slow!=fast:
        if not fast.next or not fast.next.next:
            print("无环")
            return
        slow=slow.next
        fast=fast.next.next
    print("slow和fast的相遇节点：",slow.val)#4
    #能够运行到这儿说明链表有环，接下来找入环节点：
    #fast回到head，slow保持原地，然后两者同时走，且都走一步，相遇位置即是入环节点
    fast=head
    while fast!=slow:
        fast=fast.next
        slow=slow.next
    print("有环 ，入环节点是：",slow.val)
    return slow

has_circle2(head)