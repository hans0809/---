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

#可视化
p=head
while p:
    print(p.val,p.next)
    p=p.next
#链表：0->1->2->3->4->5


print("###########################第1题###########################")
# 题目1. 输入链表头节点，奇数长度返回中点，偶数长度返回上中点

if not head or not head.next or not head.next.next:#链表为空，或者是单节点，或者只有两个节点
    print("head就是所求:",head.val)
else:#此时节点数大于2
    slow=head.next
    fast=head.next.next
    while fast.next and fast.next.next:#保证快指针走一次(两步)后的位置是链表末尾或者末尾之前，而不是空
        slow=slow.next#慢指针每次走一步
        fast=fast.next.next#快指针每次走两步
    print("slow就是所求：",slow.val)


print("###########################第2题###########################")
# 题目2. 输入链表头节点，奇数长度返回中点，偶数长度返回下中点

if not head or not head.next:#链表为空，或者是单节点
    print("head就是所求:",head.val)    
else:#此时节点数大于1
    slow=head.next
    fast=head.next
    while fast.next and fast.next.next:#保证快指针走一次(两步)后的位置是链表末尾或者末尾之前，而不是空
        slow=slow.next#慢指针每次走一步
        fast=fast.next.next#快指针每次走两步
    print("slow就是所求：",slow.val)


# 记住第一题，slow=head.next,fast=head.next.next。
# 对于第二题，由于是变成了求下中点，因此让fast左移一步，fast=head.next，同时注意修改下开始的特例即可，其余不变

print("###########################第3题###########################")
# 题目3. 输入链表头节点，奇数长度返回中点的前驱，偶数长度返回上中点的前驱

if not head or not head.next or not head.next.next:#链表为空，或者是单节点，或者只有两个节点
    print("结果是空：NULL")    
else:#此时节点数大于2
    slow=head
    fast=head.next.next
    while fast.next and fast.next.next:#保证快指针走一次(两步)后的位置是链表末尾或者末尾之前，而不是空
        slow=slow.next#慢指针每次走一步
        fast=fast.next.next#快指针每次走两步
    print("slow就是所求：",slow.val)

print("###########################第4题###########################")
# 题目4. 输入链表头节点，奇数长度返回中点的前驱，偶数长度返回下中点的前驱

if not head or not head.next:#链表为空，或者是单节点
    print("结果是空：NULL")  
elif not head.next.next:
    print("head即为所求",head.val)  #此时只有两个节点
else:#此时节点数大于2
    #两个版本，不注释的容易和其他题目对比
    slow=head
    fast=head.next
    while fast.next and fast.next.next:#保证快指针走一次(两步)后的位置是链表末尾或者末尾之前，而不是空
        slow=slow.next#慢指针每次走一步
        fast=fast.next.next#快指针每次走两步
    print("slow就是所求：",slow.val)

#总结记忆：

# 记住第一题，求上中点，slow=head.next,fast=head.next.next。
# 对于第二题，在第一题的基础上，由于变成了求下中点，因此让fast左移一步，设置slow=head.next,fast=head.next，同时注意修改下开始的特例即可，其余不变

# 对于第三题，在第一题的基础上，因为变成了求上中点的的前驱，因此让slow左移一步，设置slow=head,fast=head.next.next，同时注意修改下开始的特例即可，其余不变
# 对于第四题，在第三题的基础上，因为变成了求下中点的前驱，因此让fast左移一步，设置slow=head,fast=head.next，同时注意修改下开始的特例即可，其余不变