# 先看题目：
# 给定一个数组和一个整数num，把小于等于num的数放在数组的左边，大于num的数放在数组右边
# 要求额外空间复杂度是O(1)，时间复杂度是O(N)
# 不要求有序

# 解题：
# 设置一个遍历数组用的指针p，初始指向下标0
# 设置一个指向小于等于num区域最右侧位置的指针s，初始指向下标-1，表示还没有小于等于num的区域
# 遍历数组，如果当前下标p位置的元素小于等于num，就将该元素与
# s的后面一个位置元素做交换，然后p向右走一步，s也向右走一步
# 如果当前下标p位置的元素大于num，直接让p向右走一步，s按兵不动

def partition(arr,num):
    if len(arr)<=1:
        return 
    s=-1
    p=0
    while p<len(arr):
        if arr[p]<=num:
            arr[s+1],arr[p]=arr[p],arr[s+1]
            s+=1
            p+=1
        else:
            p+=1
arr=[11,2,1,4,5,7,3,6,1,0,3,10]
num=5
partition(arr,num)
print('partition结果：',arr)#[2, 1, 4, 5, 3, 1, 0, 3,       7, 11, 6, 10]






# 现在，升级一下题目：
# 给定一个数组和一个整数num，把小于num的数放在数组的左边，
# 等于num的数放在中间，大于num的数放在数组右边
# 要求额外空间复杂度是O(1)，时间复杂度是O(N)
# 不要求有序

# 解题：
# 设置一个遍历数组用的指针p，初始指向下标0
# 设置一个指向小于num区域最右侧位置的指针s，初始指向下标-1，表示还没有小于等num的区域
# 设置一个指向大于num区域最左侧位置的指针b，初始指向下标len(arr)，表示还没有大于num的区域
# 遍历数组，
# 1)如果当前下标p位置的元素等于num，直接让p向右走一步，其余什么也不做
# 2)如果当前下标p位置的元素小于num，就让它与s的后面一个位置元素做交换，然后p向右走一步，s也向右走一步
# 3)如果当前下标p位置的元素大于num，就让它与b的前面一个位置元素做交换，然后p按兵不动，b向左走一步

def partition2(arr,num):
    if len(arr)<=1:
        return
    s=-1
    b=len(arr)
    p=0
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
arr=[5,4,1,2,3,5,6,9,8,7,5,10]
num=5
partition2(arr,num)
print('partition2结果：',arr)






# 现在再升级一下题目，在partition2的基础上，要求返回等于num的区域的首尾下标
# 此时，只需在上面的partition2函数中，返回s+1和b-1即可
def partition3(arr,num):
    if len(arr)<=1:
        print("就{}个元素找啥找，再见".format(len(arr)))
        return
    s=-1
    b=len(arr)
    p=0
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
    return [s+1,b-1]
arr=[5,4,1,2,3,5,6,9,8,7,5,10]
num=5
res=partition3(arr,num)
print('partition3结果：',res)







# 再次升级题目，这次只给定数组arr，num就是arr中最后一个元素，
# 同样是划分成3部分(小于，等于，大于)，要求返回等于num=arr[-1]的区域的首尾下标
# 这同时也是经典的荷兰国旗问题

#直接在partition3上修改一点点即可
def partition3_NetherLandFlag(arr):
    if not arr:
        print("空数组，再见")
        return [-1,-1]#-1是错误值
    if len(arr)==1:
        return [0,0]

    s=-1
    b=len(arr)
    p=0
    num=arr[len(arr)-1]#这题的num等于arr的最后一个元素arr[-1]
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
    return [s+1,b-1]
arr=[5,4,1,2,3,5,6,9,8,7,5]
res=partition3_NetherLandFlag(arr)
print('partition3_NetherLandFlag的结果:',arr,'\n',res)


# 上述代码还可以变一下形式：
def partition3_NetherLandFlag_v2(arr):
    if not arr:
        print("空数组，再见")
        return [-1,-1]#-1是错误值
    if len(arr)==1:
        return [0,0]

    num=arr[len(arr)-1]#这题的num等于arr的最后一个元素arr[-1]
    s=-1#小于num区域的右边界
    b=len(arr)-1#大于num区域的左边界，
    # 这里暂时把num=arr[-1]包裹进了大于num的区域，但在整个while中，它都不会动
    # 也就是说，这里我只是先把num=arr[-1]放在这儿暂存
    p=0#遍历用的指针
   
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
    # 右侧区域除了最后一个(arr[-1])外，都大于num
    # 因此，只需将右侧区域最后一个元素arr[-1]与右侧区域第一个元素(左侧边界)交换，就完成了
    arr[b],arr[-1]=arr[-1],arr[b]
    # 此时，大于num区域的左边界不再是b，而是b+1
    return [s+1,b]
arr=[5,4,1,2,3,5,6,9,8,7,5]
res=partition3_NetherLandFlag_v2(arr)
print('partition3_NetherLandFlag_v2的结果:',arr,'\n',res)

