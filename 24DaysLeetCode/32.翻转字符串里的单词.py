class Solution:
    def reverseWords(self, s: str) -> str:
        dequeue=[]
        word=[]
        n=len(s)
        left=0
        right=n-1
        # 去掉首尾的空格
        while left<=right and s[left]==' ':
            left+=1
        while left<=right and s[right]==' ':
            right-=1
        while left<=right:
            # 正在遍历某个单词的字母
            if s[left]!=' ':
                word.append(s[left])
            # 一个单词已经全部记录在word中
            elif s[left]==' ' and word!=[]:
                dequeue.append(''.join(word))
                word=[]
            left+=1
        dequeue.append(''.join(word))
        return ' '.join(dequeue[::-1])