# 题目：给定一个array，求差值为k的去重数字对
# 比如 arr=[3,2,5,7,0,0]，k=2，则结果为{[0,2],[3,5],[5,7]}

def solve(arr,k):
    my_set=set()
    for num in arr:
        my_set.add(num)
    res=[]
    for cur in my_set:
        if cur+k in my_set:
            res.append((cur,cur+k))
    return res
arr=[3,2,5,7,0,0]
k=2
print("差值为{}的去重数字对:{}".format(k,solve(arr,k)))#差值为2的去重数字对:[(0, 2), (3, 5), (5, 7)]
