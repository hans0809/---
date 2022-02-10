# 给出一组区间，请合并所有重叠的区间。
# 请保证合并后的区间按区间起点升序排列。
# https://www.nowcoder.com/practice/69f4e5b7ad284a478777cb2a17fb5e6a?tpId=188&tqId=38609&rp=1&ru=/exam/oj&qru=/exam/oj&sourceUrl=%2Fexam%2Foj%3Ftab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D188%26page%3D1&difficulty=undefined&judgeStatus=undefined&tags=&title=
class Solution:
    def merge(self , intervals):
        # write code here
        if not intervals:
            return []
        intervals=sorted(intervals,key=lambda interval :interval.start)
        out=[]
        out.append(intervals[0])
        for i in range(1,len(intervals)):
            last=out[-1]
            cur_left,cur_right=intervals[i].start,intervals[i].end
            if last.end < cur_left:
                out.append(intervals[i])
            else:
                #last.start=min(last.start,cur_left)
                last.end=max(last.end,cur_right)
        return out