# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

# 枚举法超时 O(N2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        n=len(nums)

        for i in range(n):#i:[0,n]
            sum_=0
            for j in range(i,-1,-1):#j[i,0]
                sum_+=nums[j]
                if sum_==k:
                    cnt+=1
        return cnt

# 前缀和超时 O(N2)
#前缀和: 一个数组的某下标之前的所有数组元素的和（包含其自身）
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        n=len(nums)

        #存储前缀和
        pre_sum=[0]
        tmp=0
        for num in nums:
            tmp+=num
            pre_sum.append(tmp)
        print(pre_sum)
        for i in range(n):#i:[0,n]
            for j in range(i,-1,-1):#j[i,0]
                if pre_sum[i+1]-pre_sum[j]==k:#注意是i+1，因为pre_sum比nums多了一位
                    cnt+=1
        return cnt

# 哈希表+前缀和 O(N)

# 给前缀和弄一个哈希表，key是前缀和，value是前缀和出现次数
# 依据：a-b=k ==> a-k=b，只关心a-k出现次数，而不关心具体是哪些元素可以得到a-k（a在这题里面就是前缀和）
# 因为当前的前缀和是a(出现了)，而且a-k又出现过，那么一定存在b（出现了），使得a-b=k(b其实就等于a-k)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        n=len(nums)

        pre_sum_map={0:1}#前缀和哈希表，key是前缀和，value是前缀和出现次数
        # 为什么要弄个0:1 ?
        # 因为可能当前的前缀和恰好等于k，此时两者相减为0，这也算是满足题目条件的一种情况

        pre_sum=0#当前前缀和
        for i in range(n):
            pre_sum+=nums[i]#维护当前前缀和
            if pre_sum-k in pre_sum_map:#pre_sum-k相当于a-k，结果正是b(如果这个条件成立，则说明b出现过，有点类似两数之和的哈希表解法)
                cnt+=pre_sum_map[pre_sum-k]

            if pre_sum in pre_sum_map:
                pre_sum_map[pre_sum]+=1
            else:
                pre_sum_map[pre_sum]=1

        return cnt