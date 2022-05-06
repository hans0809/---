# 快排是基于Partition的
# 不同的partition方式，得到不同版本的快排




# 快排1.0版本：
# 对于输入的arr，将arr的最后一个元素看作是partition函数的num参数，并把它单独拿出来，
# 稍后处理的arr其实是arr[0:-1]，不含最后一个元素
# 对arr做partition，将arr分为两部分，左边区域小于等于num，右边区域大于num（while循环内）
# 然后将之前拿出来的元素arr[R]与大于num区域的左边界(下标为s+1，s是小于等于num区域的右边界)位置元素进行交换，
# 从而小于等于num区域的右边界从s变成s+1
# 这样，小于等于num区域的右边界一定是等于num的(左侧也可能还有num，可能挨着也可能不挨着，如果num出现次数大于1的话，但不影响)，
# 这样就确定了arr[R]的最终位置，那就是s+1
# arr[R]左边元素全部小于等于它，右边元素全部大于它，arr[R]归位
# 接下来分别递归的对左边区域和右边区域做partition即可

def partitionv_1(arr,L,R):
    if L>=R:
        return 
    num=arr[R]#枢纽
    s=L-1#指向小于等于num区域(也就是左边区域)的右边界
    p=L#遍历用的指针
    while p<R:#下标为R的元素是num，先不动它
        if arr[p]<=num:
            arr[s+1],arr[p]=arr[p],arr[s+1]
            s+=1
            p+=1
        else:
            p+=1
    #此时小于等于区域的右边界是s，s+1位置是大于num的区域的左边界
    #将arr[R]与大于num区域的左边界(下标为s+1)进行交换
    arr[s+1],arr[R]=arr[R],arr[s+1]
    #于是小于等于区域的右边界变成s+1
    #s+1位置就是元素arr[R]最终排序后的位置，之后它就不用动了
    return s+1
def quickSort_v1(arr):
    if not arr or len(arr)==1:
        return
    process_v1(arr,0,len(arr)-1)
def process_v1(arr,L,R):
    if L>=R:
        return
    M=partitionv_1(arr,L,R)#当前partition确定了一个最终位置M
    #递归的对左右两部分做partition
    process_v1(arr,L,M-1)
    process_v1(arr,M+1,R)
arr=[3,2,4,8,7,9,100,1,99,98]
quickSort_v1(arr)
print('快排1.0测试结果：',arr)# [1, 2, 3, 4, 7, 8, 9, 98, 99, 100]


# 以上是快排1.0，该方法每次都能够确定一个最终位置，即s+1，那能不能每次都确定多个最终位置呢？看快排2.0






# 快排2.0版本：
# 对于输入的arr，将arr的最后一个元素看作是partition函数的num参数，并把它单独拿出来，
# 稍后处理的arr其实是arr[0:-1]，不含最后一个元素
# 对arr做partition，将arr分为三部分，左边区域小于num，中间区域等于num，右边区域大于num（while循环内）
# 然后将之前拿出来的元素arr[R]与大于num区域的左边界(下标为b，b是大于num区域的左边界)位置元素进行交换，
def partition_v2(arr,L,R):
    if L>=R:
        return 

    num=arr[R]#枢纽num等于arr的最后一个元素，把他单独拿出来，后续处理的arr其实是arr[0:-1]
    s=L-1#s是小于num区域的右边界
    b=R#b是大于num区域的左边界，
    # 这里暂时把num=arr[R]包裹进了大于num的区域，但在整个while中，它都不会动
    # 也就是说，这里我只是先把num=arr[R]放在这儿暂存
    p=L#遍历用的指针
   
    while p<b:#退出条件，遍历用的指针p来到大于num区域左侧边界(即p=b)
        if arr[p]==num:
            p+=1
        elif arr[p]<num:
            arr[s+1],arr[p]=arr[p],arr[s+1]
            s+=1
            p+=1
        elif arr[p]>num:
            arr[p],arr[b-1]=arr[b-1],arr[p]
            b-=1
    # 此时，左侧区域全部小于num，中间区域全部等于num，
    # 右侧区域除了最后一个(arr[R])外，都大于num
    # 因此，只需将右侧区域最后一个元素arr[R]与右侧区域第一个元素(左侧边界)交换，就完成了
    arr[b],arr[R]=arr[R],arr[b]
    # 此时，大于num区域的左边界不再是b，而是b+1
    return [s+1,b]#返回等于num=arr[R]区域的左右边界，这个范围内的元素都等于arr[R]，
                  #并且都已经来到了排序后的最终位置了，之后无需再动

def quickSort_v2(arr):
    if not arr or len(arr)==1:
        return
    process_v2(arr,0,len(arr)-1)
def process_v2(arr,L,R):
    if L>=R:#base case
        return
    a,b=partition_v2(arr,L,R)#当前partition确定了一批最终位置，下标范围从a到b，闭区间
    #递归的对左右两部分做partition
    process_v2(arr,L,a-1)
    process_v2(arr,b+1,R)

arr=[3,2,4,8,7,9,100,1,99,98]
quickSort_v2(arr)
print('快排2.0测试结果：',arr)# [1, 2, 3, 4, 7, 8, 9, 98, 99, 100]






# 快排3.0版本：
# 在partition前，随机找一个下标(下标 in {0,1,2,...,R-1})，将该下标与R下标处元素交换，其余同快排2.0
# 这样做的原因在于，只有当partition后左右两部分长度相差不大时，快排的时间复杂度才是O(NlogN)，总共N个元素，每个元素找到最终位置需要做partition，
# 当partition后左右两部分长度相差不大时，partition的时间复杂度才是O(logN)
# 一个极端的例子，arr中元素恰好是逆序的，那么每做一次partition，总是只有一侧有元素，
# 此时partition的时间复杂度变成了O(N)，相应的快排时间复杂度变成了O(N^2)
# 引入随机性，可以保证快排时间复杂度是O(NlogN)
def partition_v3(arr,L,R):
    if L>=R:
        return 

    num=arr[R]#枢纽num等于arr的最后一个元素，把他单独拿出来，后续处理的arr其实是arr[0:-1]
    s=L-1#s是小于num区域的右边界
    b=R#b是大于num区域的左边界，
    # 这里暂时把num=arr[R]包裹进了大于num的区域，但在整个while中，它都不会动
    # 也就是说，这里我只是先把num=arr[R]放在这儿暂存
    p=L#遍历用的指针
   
    while p<b:#退出条件，遍历用的指针p来到大于num区域左侧边界(即p=b)
        if arr[p]==num:
            p+=1
        elif arr[p]<num:
            arr[s+1],arr[p]=arr[p],arr[s+1]
            s+=1
            p+=1
        elif arr[p]>num:
            arr[p],arr[b-1]=arr[b-1],arr[p]
            b-=1
    # 此时，左侧区域全部小于num，中间区域全部等于num，
    # 右侧区域除了最后一个(arr[R])外，都大于num
    # 因此，只需将右侧区域最后一个元素arr[R]与右侧区域第一个元素(左侧边界)交换，就完成了
    arr[b],arr[R]=arr[R],arr[b]
    # 此时，大于num区域的左边界不再是b，而是b+1
    return [s+1,b]#返回等于num=arr[R]区域的左右边界，这个范围内的元素都等于arr[R]，
                  #并且都已经来到了排序后的最终位置了，之后无需再动

def quickSort_v3(arr):
    if not arr or len(arr)==1:
        return
    process_v3(arr,0,len(arr)-1)
def process_v3(arr,L,R):
    if L>=R:#base case
        return
    
    # 随机找一个元素与arr[R]做交换
    import random
    index=random.choice(list(range(L,R)))# index in {L,L+1,L+2,...,R-2,R-1}
    arr[R],arr[index]=arr[index],arr[R]

    a,b=partition_v3(arr,L,R)#当前partition确定了一批最终位置，下标范围从a到b，闭区间
    #递归的对左右两部分做partition
    process_v3(arr,L,a-1)
    process_v3(arr,b+1,R)

arr=[3,2,4,8,7,9,100,1,99,98]
quickSort_v3(arr)
print('快排3.0测试结果：',arr)# [1, 2, 3, 4, 7, 8, 9, 98, 99, 100]