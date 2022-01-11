#题目：克隆一个无环单链表，该单链表中不仅有next指针，还有一个rand指针，它可以指向任一节点或None

#################首先创建单链表###########################
import random
class ListNode:
    def __init__(self, val=0, next=None,rand=None):
        self.val = val
        self.next = next
        self.rand=rand

nums=list(range(20))
nodes=[]
n=9
for i in range(n-1):
    index=random.choice(nums)
    nodes.append(ListNode(index))

head=ListNode(10)
p=head
for i in range(n-1):
    p.next=nodes[i]
    p.rand=random.choice(nodes+[None])
    p=nodes[i]

#可视化next方向
def my_print(head,desc):
    print(desc,end=":")
    p=head
    while p:
        print(p.val,end="->")
        p=p.next
    print("None")
#可视化rand方向
def my_print2(head,desc):
    print(desc,end=":")
    p=head
    while p:
        if p.rand is not None: 
            print(p.rand.val,end=" ")
        else:
            print('None',end=' ')
        p=p.next
    print("None")
my_print(head,'原链表next方向')
my_print2(head,'原链表rand方向')
# 原链表next方向:10->1->6->12->15->10->10->2->5->None
# 原链表rand方向:5 None 10 None 12 None 1 1 None None


########################笔试解题#########################

#用哈希表存储{(原始节点1，克隆节点1),(原始节点2，克隆节点2),...}
def solution1(head):
    dic={}
    
    #存起来，(key：旧节点，value：新节点)
    #并对新节点的val赋值
    p=head
    while p:
        dic[p]=ListNode(p.val)
        p=p.next

    #对新节点的next方向和rand方向进行赋值
    p=head
    while p:
        #p:旧节点; dic[p]:新节点
        # 这里一定要用get，因为当p来到末尾时，p.next=None，而None不是dic的key，
        # 此时只需返回None即可，即None对应的value为None
        dic[p].next=dic.get(p.next,None)
        dic[p].rand=dic.get(p.rand,None)

        p=p.next

    #可视化一下
    my_print(head,'克隆链表next方向')
    my_print2(dic[head],'克隆链表rand方向') 

    return dic[head]

# solution1(head)


########################面试解题#########################

# 1.将链表1->2搞成1->1'->2->2'的形式，其中'代表该节点 是 对应的 不带'的节点 的克隆节点，
# 这一步只对克隆节点的val进行赋值

# 2.对克隆节点的rand方向进行赋值：由于每一个原节点的next指向其对应的克隆节点(比如2指向2')，
# 因此，克隆的节点的rand指向，就等于原节点的rand指向的next。
# 比如，克隆的节点2(即2')的rand指向，就等于原节点2的rand指向的next

# 3.拆分出克隆链表，即对克隆节点的next方向进行赋值

def solution2(head):
    #第1步，对克隆节点的val进行赋值，在next方向：1->2->None 变成1->1'->2->2'->None
    p=head
    next=head
    while p:
        next=p.next
        
        ############
        p.next=ListNode(p.val)
        p.next.next=next
        ############

        p=next
    #可视化看看
    my_print(head,'第1步的结果')

    #第2步：对克隆节点的rand方向进行赋值，此时链表next方向为：1->1'->2->2'->None
    p=head
    next=head
    while p:
        next=p.next.next#p.next总不为空，而是p对应的克隆节点

        #########################
        cloneNode=p.next
        if p.rand:
            cloneNode.rand=p.rand.next
        else:#p.rand 为None
            cloneNode.rand=None
        ##########################
       
        p=next

    #可视化看看
    my_print2(head,'第2步的结果(整个大链表rand方向)')

    #第3步：对克隆节点的next方向进行赋值，即:将1->1'->2->2'拆分为1->2和1'->2'
    #由于rand方向已经在第2步搞定，所以这里只考虑next方向即可

    #旧
    p=head
    next=head

    cloneHead=p.next#克隆链表的头节点

    #新(克隆)
    cp=cloneHead
    cnext=cloneHead

    while p:
        if p.next:
            next=p.next.next
            p.next=next
        else:
            p.next=None
        
        if cp.next:
            cnext=cp.next.next
            cp.next=cnext
        else:
            cp.next=None
        
        p=p.next
        cp=cp.next
    
    #可视化第3步结果
    my_print(cloneHead,'第3步的结果(拆分得到的克隆链表的next方向)')

solution2(head)
