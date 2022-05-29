# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
# 分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )


class CQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

        return None

    def deleteHead(self) -> int:
        if not self.stack2 and not self.stack1:
            return -1
        if self.stack2:
            ret=self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            ret=self.stack2.pop()
        return ret



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()