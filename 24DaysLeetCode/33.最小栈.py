class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[math.inf]#min_stack的栈顶就是stack的最小值, 因此查最小值只需常数时间

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val,self.min_stack[-1]))


    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()