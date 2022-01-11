# 题目：给定两个可能有环也可能无环的单链表，判定这两个链表是否相交，
# 若相交，返回相交的第一个节点

#################首先创建单链表###########################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def my_print(head,desc):
    print(desc,end=":")
    p=head
    while p:
        print(p.val,end="->")
        p=p.next
    print("None")

# 创建两个链表都是无环且相交的链表
nodes=[ListNode(i) for i in range(1,15)]

head1=ListNode(0)
p1=head1
p1.next=nodes[1]
p1=p1.next
p1.next=nodes[2]
p1=p1.next
p1.next=nodes[3]
p1=p1.next
p1.next=nodes[4]
p1=p1.next

head2=ListNode(0)
p2=head2
p2.next=nodes[5]
p2=p2.next
p2.next=nodes[6]
p2=p2.next
p2.next=nodes[3]
p2=p2.next


#可视化
my_print(head1,"无环链表head1")# 0->2->3->4->5->None
my_print(head2,"无环链表head2")# 0->6->7->4->5->None
"""
head1->nodes[1]->nodes[2]->nodes[3]->nodes[4]
                           ↗
head2->nodes[5]->nodes[6] 
"""

# 创建两个链表都是无环且不相交的链表
nodes=[ListNode(i) for i in range(1,15)]

head3=ListNode(0)
p1=head3
p1.next=nodes[1]
p1=p1.next
p1.next=nodes[2]
p1=p1.next
p1.next=nodes[3]
p1=p1.next
p1.next=nodes[4]
p1=p1.next

head4=ListNode(0)
p2=head4
p2.next=nodes[5]
p2=p2.next
p2.next=nodes[6]
p2=p2.next


#可视化
my_print(head3,"无环链表head3")# 0->2->3->4->5->None
my_print(head4,"无环链表head4")# 0->6->7->None
"""
head3->nodes[1]->nodes[2]->nodes[3]->nodes[4]
                           
head4->nodes[5]->nodes[6] 
"""


#然后实现判断链表是否有环的函数（直接用`链表有无环的判定.py`中实现好的）

#####################笔试解法：哈希set###########################

def has_circle1(head):
    if not head or not head.next or not head.next.next:#空或者单节点或者只有两个节点
        print("无环")
        return
    hashset=set()
    p=head
    while p:
        #print(p.val,end='->')
        if p in hashset:
            print("有环，入环节点是：",p.val)
            return p
        hashset.add(p)
        p=p.next
    print("无环")
    return
# has_circle1(head1)
# print("******************")
# has_circle1(head2)

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



# 有了判断链表是否有环的函数，接下来开始解题

# 分3种情况：

# 1. 两个链表都无环：
# 此时，如果这两个链表的尾节点不是同一个节点，则不相交，
# 如果尾节点是同一个节点，则相交，则必然共用最后的公共部分（图1）
# 因为next指向是唯一的，因此不可能在相交后再分出一个叉（图2）
# 图1是对的，图2是错的
"""
图1:

*             
  *          *
    *       *
        *
        *
        *
       
图2:

*             
  *          *
    *       *
        *
        *
        *
      *   *
            *
"""
# 所以，只需要判断这两个链表的尾节点是否是同一个节点，如果不是，则不相交
# 如果是，那么说明两个链表相交，那么就需要找它们第一个相交的节点：
# 假设两个链表的长度分别为20和10，那么让长度为10的链表先走10步，
# 然后这两个链表再一起走，它们第一次相遇的节点就是第一个相交节点
def bothNoCircle(head1,head2):
    if not head1 or not head2:#至少有一个为空链表，则不相交
        print("两个链表不相交")
        return
    p1=head1
    p2=head2
    len1=1#第一个链表的长度
    len2=1#第二个链表的长度
    while p1.next:
        len1+=1
        p1=p1.next
    while p2.next:
        len2+=1
        p2=p2.next

    #此时，p1指向第一个链表的尾节点，p2指向第二个链表的尾节点
    
    #如果尾节点不是同一个，则不相交
    if p1!=p2:
        print("两个链表不相交")
        return 
    
    #如果尾节点是同一个，那么说明两个链表相交，就需要找第一个相交的节点

    #让p1指向长的链表，p2指向短的链表, len1代表长的链表的长度，len2代表短的链表的长度
    if len1<len2:
        p1=head2
        p2=head1
        len1,len2=len2,len1
    else:
        p1=head1
        p2=head2
    
    gap=len1-len2
    #先让长的链表走gap步
    for _ in range(gap):
        p1=p1.next
    #然后两个链表再一起走，第一次相遇的节点就是第一个相交的节点
    while p1!=p2:
        p1=p1.next
        p2=p2.next

    print("相交，第一个相交的节点是：",p1.val)
    return p1

#测试bothNoCircle
# print("#############################")
# print("判定head1和head2：")
# bothNoCircle(head1,head2)
# print("#############################")
# print("判定head3和head4：")
# bothNoCircle(head3,head4)

#2. 两个链表只有一个有环：此时一定不相交
# 因为next的指向具有唯一性，下图中右侧无环链表无论是接在左边有环链表的上面(next一个往下指，一个指向None)，
# 还是接在下面的环中(next指向两个不同的节点)，都会破坏这种唯一性
"""
     *        *
     *        *
     *        *
    *
 *    *
  *   *
    *
"""

#3.两个链表都都有环：
# 此时又可细分为3种情况：
# 3.1：两个有环链表相互独立
"""
*       *
*       *
*       * * * 
* *     *   *
* *     * * *
"""
#3.2：两个有环链表的入环节点是同一个节点
"""
        *
        * 
  *     *
  *    *
  *  *
  *(同一个入环节点)   
*   *
*   *
* * *   
"""
#3.3：两个有环链表的入环节点不是同一个节点
"""
         *
         * 
  *      *
  *      *
  *      *
  *(1)   *
*   *   *
* (2)* * 
* * *  
"""

# 可以看到，此时如果两个有环链表相交，那么它们一定共用同一个环，唯一的区别就是第一次入环节点是不是同一个

def bothCircle(head1,head2,loop1,loop2):#loop1和loop分别是两个链表第一次入环时的节点
    #如果两个有环链表第一次入环时的节点是同一个，则对应情况3.2，假设是节点m，那么节点m之前会有两个岔路，分别对应两个链表未入环的部分
    #此时，可以套用情况1，只需要把情况1中的尾节点改成这里的节点m即可
    if loop1==loop2:
        p1=head1
        p2=head2
        len1=1#第一个链表的长度
        len2=1#第二个链表的长度
        while p1!=loop1:
            len1+=1
            p1=p1.next
        while p2!=loop2:
            len2+=1
            p2=p2.next

        #此时，p1和p2都指向第一个入环节点

        #找第一个相交的节点

        #让p1指向长的链表，p2指向短的链表, len1代表长的链表的长度，len2代表短的链表的长度
        if len1<len2:
            p1=head2
            p2=head1
            len1,len2=len2,len1
        else:
            p1=head1
            p2=head2
        
        gap=len1-len2
        #先让长的链表走gap步
        for _ in range(gap):
            p1=p1.next
        #然后两个链表再一起走，第一次相遇的节点就是第一个相交的节点
        while p1!=p2:
            p1=p1.next
            p2=p2.next

        print("相交，第一个相交的节点是：",p1.val)
        return p1
    #若入环节点不是同一个
    else:
        #则让loop1一直走，
        # 若loop又回到了loop1，则对应情况3.1：两个有环链表相互独立
        # 若loop1遇到了loop2，则对应情况3.3：两个有环链表的入环节点不是同一个节点但相交
        p1=loop1.next
        while(p1!=loop1):
            if p1==loop2:
                print("相交，第一个相交的节点是：",loop1.val)#对应情况3.3
                return loop1
            p1=p1.next
        print("两个链表不相交")#对应情况3.1
        return

# 现在定义main函数
def mainfunc(head1,head2):
    loop1=has_circle2(head1)
    loop2=has_circle2(head2)

    #两个链表都无环
    if not loop1 and not loop2:
        print("两个链表都无环，调用bothNoCircle函数，结果如下：")
        return bothNoCircle(head1,head2)

    #两个链表都有环
    if loop1 and loop2:
        print("两个链表都有环，调用bothCircle函数，结果如下：")
        return bothCircle(head1,head2,loop1,loop2)

    #一个有环，一个无环
    print("两个链表一个有环，一个无环，两者不可能相交")
    return 
    
print("#############都无环，相交测试####################")
mainfunc(head1,head2)
print("#############都无环，不相交测试####################")
mainfunc(head3,head4)
"""
无环链表head1:0->2->3->4->5->None
无环链表head2:0->6->7->4->5->None
无环链表head3:0->2->3->4->5->None
无环链表head4:0->6->7->None
#############相交测试####################       
无环
无环
两个链表都无环，调用bothNoCircle函数，结果如下：
相交，第一个相交的节点是： 4
#############不相交测试####################     
无环
无环
两个链表都无环，调用bothNoCircle函数，结果如下：
两个链表不相交
"""