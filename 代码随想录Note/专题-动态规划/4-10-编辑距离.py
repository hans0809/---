# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符


# dp[i][j] 表示以下标i-1为结尾的字符串word1，和以下标j-1为结尾的字符串word2，最近编辑距离为dp[i][j]。

# 2. 确定递推公式
# 在确定递推公式的时候，首先要考虑清楚编辑的几种操作，整理如下：

# if (word1[i - 1] == word2[j - 1])
#     不操作
# if (word1[i - 1] != word2[j - 1])
#     增
#     删
#     换

# if (word1[i - 1] == word2[j - 1]) 那么说明不用任何编辑，dp[i][j] 就应该是 dp[i - 1][j - 1]，即dp[i][j] = dp[i - 1][j - 1];

# 此时可能有同学有点不明白，为啥要即dp[i][j] = dp[i - 1][j - 1]呢？

# 那么就在回顾上面讲过的dp[i][j]的定义，word1[i - 1] 与 word2[j - 1]相等了，那么就不用编辑了，以下标i-2为结尾的字符串word1和以下标j-2为结尾的字符串word2的最近编辑距离dp[i - 1][j - 1]就是 dp[i][j]了。

# 在下面的讲解中，如果哪里看不懂，就回想一下dp[i][j]的定义，就明白了。

# 在整个动规的过程中，最为关键就是正确理解dp[i][j]的定义！

# if (word1[i - 1] != word2[j - 1])，此时就需要编辑了，如何编辑呢？

# 操作一：word1删除一个元素，那么就是以下标i - 2为结尾的word1 与 j-1为结尾的word2的最近编辑距离 再加上一个操作。
# 即 dp[i][j] = dp[i - 1][j] + 1;

# 操作二：word2删除一个元素，那么就是以下标i - 1为结尾的word1 与 j-2为结尾的word2的最近编辑距离 再加上一个操作。
# 即 dp[i][j] = dp[i][j - 1] + 1;

# 这里有同学发现了，怎么都是删除元素，添加元素去哪了。

# word2添加一个元素，相当于word1删除一个元素，例如 word1 = "ad" ，word2 = "a"，word1删除元素'd' 和 word2添加一个元素'd'，变成word1="a", word2="ad"， 最终的操作数是一样！

# 操作三：替换元素，word1替换word1[i - 1]，使其与word2[j - 1]相同，此时不用增加元素，那么以下标i-2为结尾的word1 与 j-2为结尾的word2的最近编辑距离 加上一个替换元素的操作。

# 即 dp[i][j] = dp[i - 1][j - 1] + 1;

# 综上，当 if (word1[i - 1] != word2[j - 1]) 时取最小的，即：dp[i][j] = min({dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]}) + 1;

# 3. dp数组如何初始化
# 再回顾一下dp[i][j]的定义：

# dp[i][j] 表示以下标i-1为结尾的字符串word1，和以下标j-1为结尾的字符串word2，最近编辑距离为dp[i][j]。

# 那么dp[i][0] 和 dp[0][j] 表示什么呢？

# dp[i][0] ：以下标i-1为结尾的字符串word1，和空字符串word2，最近编辑距离为dp[i][0]。

# 那么dp[i][0]就应该是i，对word1里的元素全部做删除操作，即：dp[i][0] = i;

# 同理dp[0][j] = j;

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1,n2=len(word1),len(word2)
        #dp[i][j]:word1[0...i-1]和word2[0...j-1]的最近编辑距离
        dp=[[0 for _ in range(n2+1)] for _ in range(n1+1)]

        # dp初始化
        dp[0][0]=0#都是空串时,啥也不用做就一样了,编辑距离是0
        # 当两个字符串其中任意一个为空时,最近的编辑距离就是不为空的那个串的长度
        for i in range(1,n1+1):
            dp[i][0]=i
        for j in range(1,n2+1):
            dp[0][j]=j
        
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:# 添加或替换一个元素
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[n1][n2]