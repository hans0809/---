# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

# 示例: 输入："23" 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# 说明：尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)
        if n==0:
            return []
        digit2letter={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        res=[]
        s=[]
        def backtrack(digits,index):
            #index:当前应该遍历第几个数字对应的字符串，即digit2letter[digits[index]]
            if len(s)==n:
                res.append(''.join(s))
                return
            
            letter=digit2letter[int(digits[index])]
            for ch in letter:
                s.append(ch)
                backtrack(digits,index+1)
                s.pop()

        backtrack(digits,0)

        return res