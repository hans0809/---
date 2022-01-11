# 首先来建堆，以大根堆为例，数组下标从0开始
# 对于下标为i的节点，其父节点的下标为(i-1)/2，
# 其左孩子的下标为2*i+1，其右孩子的下标为2*i+2

# 比如a_simple_heap=[9,8,6,3,4,5]
#               下标:0,1,2,3,4,5

"""
使用a_simple_heap可以建立一个大根堆:

      9
   8     6
 3   4 5

 对应存储堆的数组就是[9,8,6,3,4,5]
"""

#现在，打乱a_simple_heap中元素的顺序，得到一个数组arr，希望据此建立一个大根堆
arr=[8,9,6,4,5,3]
print("###################### 大根堆###################")
# 先定义插入节点的函数push()，然后对arr中的每一个元素调用该函数即可完成建堆操作
heapMaxSize=8#堆所能容纳的最大节点数，是一个常量
heap=[]
heapSize=0#当前堆内的节点数，是一个变量，heapSize始终指向下一个新插入元素的下标

def push(value):
    global  heapSize#可以修改heapSize的值
    #如果堆满了
    if heapSize==heapMaxSize:
        print("堆满，无法插入新的节点到堆中")
        return -1
    #如果堆还没有满，那么就可以在堆中插入一个元素值等于value的节点了
    heap.append(value)#将新节点的值记录到heap数组中
    heapInsert(heapSize)#执行真正的插入节点操作
    heapSize+=1#堆中元素个数加1

    #print(heap)

#插入元素的过程是一个不断上浮的过程
def heapInsert(index):#index：待插入元素在建好的堆对应的数组heap中的下标
    #只要待插入节点的值大于其父节点的值，就一直执行这个循环(插入节点上浮)
    #退出循环的条件：heap[index]!>heap[(index-1)//2] 或者 index==0
    while heap[index]>heap[int((index-1)/2)]:#!!注意Python中-0.5//2=-1而不是0，导致调了很久，坑！！
        #此时待插入节点元素的值大于其父节点的值，交换两者，即：待插入节点上浮
        heap[index],heap[(index-1)//2]=heap[int((index-1)/2)],heap[(index)]
        index=int((index-1)/2)#待插入节点上浮后的位置

# 现在，使用arr来建立一个大根堆heap
for element in arr:
    push(element)

#这样就建好了一个大根堆，可以查看一下存储堆的数组
print('建立的大根堆如下：',heap)#[9, 8, 6, 4, 5, 3]
print('堆中元素个数为：',heapSize)#6


# 现在已经建好了一个堆，希望能够找到堆中的最大值，将其拿出来(在堆中删掉)，并且要保证剩余元素仍然是一个堆
def pop():
    global heapSize#可以修改heapSize的值

    #第一个元素是最大的, 交换第一个和最后一个元素
    heap[0],heap[heapSize-1]=heap[heapSize-1],heap[0]
    #此时最大值处于最后一个元素位置(下标为heapSize-1)
    #将最大值元素拿出来
    ret=heap.pop()
    #heapsize减一,因为拿出来了一个元素嘛，所以-1
    heapSize=heapSize-1
    
    #此时的heap不再是一个堆，因此需要做相应调整，使其仍是一个堆
    index=0#最后一个节点被交换到了第一个节点，下标为0
    # 因此就从这第一个节点（下标为0）开始，向下看，
    # 只要发现自己有孩子节点的值比自己大，那么就让孩子节点上位，自己下沉，然后继续看自己的孩子节点是否比自己大
    # 如果自己的孩子节点都不比自己大，那么就可以停止下沉了，此时heap是一个堆
    # 以上步骤由heapify函数完成
    heapify(index)

    return ret
def heapify(index):
    left=2*index+1#左孩子的下标，因此右孩子的下标是left+1

    #如果左孩子下标!<heapSize，那么右孩子的下标(等于左孩子下标+1)自然也!<heapSize，因此就不用额外判断了
    #如果左孩子下标<heapSize，则右孩子的下标是否<heapSize需要进一步判断
    #始终要明确：heapSize恰好是堆中所含元素的个数，但是由于下标是要-1的，因此堆中最后一个元素的下标是heapSize-1
    while left<heapSize:
        #找到左右孩子中元素值较大的那个(前提是孩子存在，当然，既然进入了这个循环，那么左孩子肯定存在了，只需要判断一下右孩子是否存在)
        right=left+1#右孩子的下标(如果右孩子存在)
        #右孩子存在时，比较左右孩子的值，将值最大的那个节点的下标给largest
        if right<heapSize:
            if heap[right]>heap[left]:
                largest=right
            else:
                largest=left
        #此时右孩子不存在，直接将左孩子的下标给largest
        else:
            largest=left
        
        #找到了当前节点的孩子节点中的较大值所在下标max_index后，比较一下当前位置（下标为index）节点和下标为max_index的节点的元素值的大小
        #如果当前位置节点元素值<下标为max_index的元素值，就交换两者，当前节点会下沉
        if heap[largest]>heap[index]:
            heap[largest],heap[index]=heap[index],heap[largest]#交换，较大元素值对应的节点上浮 
            index=largest#当前节点下沉，跟踪index
            left=2*index+1#下沉后节点的左孩子下标
        else:
            break

# print("取出堆中的最大值为：",pop())
# print('取出最大元素后的堆：',heap)


# 堆排序“大根堆
sortRes=[]
for _ in range(len(heap)):
    sortRes.append(pop())
print('堆排序得到的结果：',sortRes)#[9, 8, 6, 5, 4, 3]


        




######################################## 以上是大根堆，小根堆同理#####################################

#现在，打乱a_simple_heap中元素的顺序，得到一个数组arr，希望据此建立一个小根堆
arr=[8,9,6,4,5,3]
print("###################### 小根堆###################")
# 先定义插入节点的函数push()，然后对arr中的每一个元素调用该函数即可完成建堆操作
heapMaxSize=8#堆所能容纳的最大节点数，是一个常量
heap=[]
heapSize=0#当前堆内的节点数，是一个变量，heapSize始终指向下一个新插入元素的下标

def push(value):
    global  heapSize#可以修改heapSize的值
    #如果堆满了
    if heapSize==heapMaxSize:
        print("堆满，无法插入新的节点到堆中")
        return -1
    #如果堆还没有满，那么就可以在堆中插入一个元素值等于value的节点了
    heap.append(value)#将新节点的值记录到heap数组中
    heapInsert(heapSize)#执行真正的插入节点操作
    heapSize+=1#堆中元素个数加1

    #print(heap)

#插入元素的过程是一个不断上浮的过程
def heapInsert(index):#index：待插入元素在建好的堆对应的数组heap中的下标
    #只要待插入节点的值大于其父节点的值，就一直执行这个循环
    #退出循环的条件：heap[index]!<heap[(index-1)//2] 或者 index==0
    while heap[index]<heap[int((index-1)/2)]:#!!注意python中-0.5//2=-1而不是0，导致调了很久，坑！！
        #此时待插入节点元素的值大于其父节点的值，交换两者，即：待插入节点上浮
        heap[index],heap[(index-1)//2]=heap[int((index-1)/2)],heap[(index)]
        index=int((index-1)/2)#待插入节点上浮后的位置

# 现在，使用arr来建立一个大根堆heap
for element in arr:
    push(element)

#这样就建好了一个大根堆，可以查看一下存储堆的数组
print('建立的小根堆如下：',heap)#[9, 8, 6, 4, 5, 3]
print('堆中元素个数为：',heapSize)#6


# 现在已经建好了一个堆，希望能够找到堆中的最大值，将其拿出来(在堆中删掉)，并且要保证剩余元素仍然是一个堆
def pop():
    global heapSize#可以修改heapSize的值

    #第一个元素是最大的, 交换第一个和最后一个元素
    heap[0],heap[heapSize-1]=heap[heapSize-1],heap[0]
    #此时最大值处于最后一个元素位置(下标为heapSize-1)
    #将最大值元素拿出来
    ret=heap.pop()
    #heapsize减一,因为拿出来了一个元素嘛，所以-1
    heapSize=heapSize-1
    
    #此时的heap不再是一个堆，因此需要做相应调整，使其仍是一个堆
    index=0#最后一个节点被交换到了第一个节点，下标为0
    # 因此就从这第一个节点（下标为0）开始，向下看，
    # 只要发现自己有孩子节点的值比自己大，那么就让孩子节点上位，自己下沉，然后继续看自己的孩子节点是否比自己大
    # 如果自己的孩子节点都不比自己大，那么就可以停止下沉了，此时heap是一个堆
    # 以上步骤由heapify函数完成
    heapify(index)

    return ret
def heapify(index):
    left=2*index+1#左孩子的下标，因此右孩子的下标是left+1

    #如果左孩子下标!<heapSize，那么右孩子的下标(等于左孩子下标+1)自然也!<heapSize，因此就不用额外判断了
    #如果左孩子下标<heapSize，则右孩子的下标是否<heapSize需要进一步判断
    #始终要明确：heapSize恰好是堆中所含元素的个数，但是由于下标是要-1的，因此堆中最后一个元素的下标是heapSize-1
    while left<heapSize:
        #找到左右孩子中元素值较大的那个(前提是孩子存在，当然，既然进入了这个循环，那么左孩子肯定存在了，只需要判断一下右孩子是否存在)
        right=left+1#右孩子的下标(如果右孩子存在)
        #右孩子存在时，比较左右孩子的值，将值最小的那个节点的下标给smallest
        if right<heapSize:
            if heap[right]<heap[left]:
                smallest=right
            else:
                smallest=left
        #此时右孩子不存在，直接将左孩子的下标给smallest
        else:
            smallest=left
        
        #找到了当前节点的孩子节点中的较小值所在下标min_index后，比较一下当前位置（下标为index）节点和下标为min_index的节点的元素值的大小
        #如果当前位置(下标为index)节点元素值<下标为min_index的元素值，就交换两者，当前节点会下沉
        if heap[smallest]<heap[index]:
            heap[smallest],heap[index]=heap[index],heap[smallest]#交换，较小元素值对应的节点上浮 
            index=smallest#当前节点下沉，跟踪其下标index
            left=2*index+1#下沉后节点的左孩子下标
        else:
            break

# print("取出堆中的最小值为：",pop())
# print('取出最小元素后的堆：',heap)


# 堆排序：小根堆
sortRes=[]
for _ in range(len(heap)):
    sortRes.append(pop())
print('堆排序得到的结果：',sortRes)#[3, 4, 5, 6, 8, 9]


# 时间复杂度：O(NlogN)










