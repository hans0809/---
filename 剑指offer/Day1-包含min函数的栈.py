class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.stack_min=[]# 栈顶始终是stack的最小值        


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.stack_min or x<=self.stack_min[-1]:# 必须加等号！！！
            self.stack_min.append(x)


    def pop(self) -> None:
        if self.stack.pop()==self.stack_min[-1]:
            self.stack_min.pop()
        
    def top(self) -> int:
        return self.stack[-1]


    def min(self) -> int:
        return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()