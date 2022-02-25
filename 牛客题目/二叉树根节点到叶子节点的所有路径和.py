# https://www.nowcoder.com/practice/185a87cd29eb42049132aed873273e83?tpId=117&tqId=37715&rp=1&ru=/exam/oj&qru=/exam/oj&sourceUrl=%2Fexam%2Foj%3Ftab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D117&difficulty=undefined&judgeStatus=undefined&tags=&title=

# 回溯法
class Solution:
    def sumNumbers(self , root):
        # write code here
        sums=[]
        def pre_order(root,sumstr):
            if not root:
                return 
            # 开始回溯
            sumstr+=str(root.val)
            # 如果来到叶子节点，就找到了一条路径，将此时的 路径组成值 添加到结果列表sums中
            if not root.left and not root.right:
                sums.append(int(sumstr))

            pre_order(root.left,sumstr)
            pre_order(root.right,sumstr)
            
            # 恢复回溯前的状态
            sumstr=sumstr[:-1]

        sumstr=''
        pre_order(root,sumstr)
        return sum(sums)