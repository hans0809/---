# 有若干样本a,b,c,d,...,类型假设是V
# 在并查集中一开始认为每个样本都在单独的集合里
# 用户可以在任何时候调用如下两个方法：
# 1)isSameSet(V x, V y):查询样本x和一般y是否属于同一个集合
# 2)union(V x,V y):把x和y各自所在集合的所有样本合并成一个集合
# isSameSet和union方法的代价越低越好

# 在并查集中，每个集合用一个样本表示，这个样本是代表点，该集合内所有其它样本都直接或间接的指向代表点
# 在下面的实现中，当findFather被调用后，每个样本都直接指向代表点，
# 因此代表点的size(用sizeMap存储)就代表了该代表点所在集合中的样本数
# sizeMap中的总的键值对数就是总的集合数
################### 创建并查集数据结构######################
class V:
    def __init__(self,obj):
        self.obj = obj

class UnionSet:
    def __init__(self):
        # (val,node)      node=V(val)
        self.nodes=dict()
        # (node:node's parent)
        self.parents=dict()
        # (node,size)# node是代表点，代表整个集合，
        # 集合中所有元素都指向这个代表点
        self.sizeMap=dict()
    
    # 给一堆元素值，创建一个并查集
    def unionSet(self, values):
        for value in values:
            node=V(value)
            self.nodes[value]=node
            self.parents[node]=node
            self.sizeMap[node]=1
    # 从cur往上找，找到不能再往上的代表点，返回
    def findFather(self,cur):
        path=[]
        while cur != self.parents[cur]:
            path.append(cur)
            cur=self.parents[cur]
        # 优化，让查找parent走更少的路
        while path:
            self.parents[path.pop()]=cur
        return cur
        
    def isSameSet(self,a,b):
        if a not in self.nodes or b not in self.nodes:
            return
        return self.findFather(self.node[a])==self.findFather(self.node[b])
    
    def union(self,a,b):
        if a not in self.nodes or b not in self.nodes:
            return
        aHead=self.findFather(self.nodes[a])
        bHead=self.findFather(self.nodes[b])
        
        if aHead!=bHead:
            aSetSize=self.sizeMap[aHead]
            bSetSize=self.sizeMap[bHead]
            big=aHead if aSetSize>=bSetSize else bHead
            small =bHead if big==aHead else aHead

            self.parents[small]=big
            self.sizeMap[big]=aSetSize+bSetSize
            del self.sizeMap[small] 
    #总的集合数 
    def getSizeMap(self):
        return len(self.sizeMap.keys())


# 题目：每个用户各含3个字段，只要两个用户有一个字段一样，就说明这两个用户是一个用户，求总共有几个用户

class Person:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

def mergeUsers(users):
    unionFind=UnionSet()
    # 使用users创建并查集
    unionFind.unionSet(users)

    mapA=dict()
    mapB=dict()
    mapC=dict()

    for user in users:
        if user.a in mapA:
            unionFind.union(user,mapA[user.a])
        else:
            mapA[user.a]=user
        if user.b in mapB:
            unionFind.union(user,mapB[user.b])
        else:
            mapB[user.b]=user
        if user.c in mapC:
            unionFind.union(user,mapC[user.c])
        else:
            mapC[user.c]=user
    
    return unionFind.getSizeMap()

users=[Person(1,'Bob',3),Person(2,'Bob',4),Person(3,'Mary',6)]
print('users中总共有{}个不同的用户'.format(mergeUsers(users)))#2
        

