#题目：将单链表按某个值划分成左边小，中间相等，右边大的形式

#################首先创建单链表###########################
import random
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

nums=list(range(20))
nodes=[]
n=9
for i in range(n-2):
    index=random.choice(nums)
    nodes.append(ListNode(index))
#按照10分区，小于10放左边，等于10放中间 ，大于10放右边
head=ListNode(10)
head.next=ListNode(10)
p=head.next
for i in range(n-2):
    p.next=nodes[i]
    p=nodes[i]

#可视化
def my_print(head,desc):
    print(desc,end=":")
    p=head
    while p:
        print(p.val,end="->")
        p=p.next
    print("None")
my_print(head,'原链表')
#链表：10->10->8->13->7->14->4->0->10->None 每次都是随机的

####################面试解题##############################
#将链表划分成3段，小于element，等于element，大于element，分别记录每一段的头节点和尾节点
def solution(head,element=10):
    if not head or not head.next:#空或者单节点
        return head

    s_head,s_tail=None,None#小于element的头和尾
    e_head,e_tail=None,None#等于element的头和尾
    b_head,b_tail=None,None#大于element的头和尾

    #遍历原链表，将其划分成3个子链表，分别对应题目要求的3个分区
    p=head#工作指针
    next=head#指向p的后继节点
    while p:#此时节点数大于1
        next=p.next#p的后继节点，先存起来，因为稍后当前p指向的节点会被砍下来
        p.next = None#把当前节点砍下来

        #左侧分区
        if p.val <element:
            if s_head is None and s_tail is None:
                s_head =p
                s_tail =p
            else:#头节点不变，在尾节点后面继续添加
                s_tail.next =p
                s_tail=s_tail.next
        #中间分区
        elif p.val==element:
            if e_head is None and e_tail is None:
                e_head =p
                e_tail =p
            else:
                e_tail.next=p
                e_tail=e_tail.next
        #右侧分区
        elif p.val>element:
            if b_head is None and b_tail is None:
                b_head =p
                b_tail =p
            else:
                b_tail.next=p
                b_tail=b_tail.next

        p=next#工作指针后移，准备处理下一个节点
    
    #看一下每个分区
    my_print(s_head,'左侧分区')
    my_print(e_head,'中间分区') 
    my_print(b_head,'右侧分区')   

    #将3个分区连起来，注意某个分区可能不存在的情况，比如element=10，但是链表中没有小于10的元素，则左侧分区不存在
    dummyHead=ListNode()
    p=dummyHead
    #如果左侧分区存在
    if s_head is not None:#等价于if s_tail is not None
        p.next =s_head
        p=s_tail

        #如果中间分区存在
        if e_head is not None:
            p.next=e_head
            p=e_tail

            p.next=b_head#指向右侧分区子链表的头节点，不用管它存不存在

        #如果中间分区不存在，直接指向右侧分区子链表的头节点，不用管它存不存在
        else:
            p.next = b_head

    #如果左侧分区不存在
    else:
        #如果中间分区存在
        if e_head is not None:#等价于if e_tail is not None
            p.next = e_head
            p=e_tail

            p.next=b_head#指向右侧分区子链表的头节点，不用管它存不存在

        #如果中间分区也不存在，直接指向右侧分区子链表的头节点，不用管它存不存在
        else:
            p.next = b_head

    #看一下结果
    my_print(dummyHead.next,'划分后')

    return dummyHead.next
        
#运行
solution(head,element=10)#element=10,1,100


#此外，还有笔试解法
            














