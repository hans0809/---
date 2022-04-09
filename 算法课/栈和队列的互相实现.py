# 两个栈实现一个队列
# 思路：准备两个栈，一个用于push，一个用于pop
# 将push栈的元素倒入pop栈，遵循如下两条原则：
# 1)push栈倒数据要一次倒完；2)push栈倒数据时要先检查pop栈，只有pop栈为空时才能倒入
class myQueue():
    pushStack=[]
    popStack=[]
    def push(self,element):
        self.pushStack.append(element)
        self.dao()
    def pop(self):
        if not self.popStack and not self.pushStack:
            print("空")
            return
        self.dao()# 可能有新的元素进入了push栈，所以要检查一下
        self.popStack.pop()
        
    def dao(self):
        # pop stack为空时才倒入
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())

queue=myQueue()
queue.push(2)
queue.push(6)
queue.push(3)
print(queue.pushStack,queue.popStack)
queue.pop()
print(queue.pushStack,queue.popStack)
queue.pop()
print(queue.pushStack,queue.popStack)
queue.pop()


# 用两个队列实现栈
# 思路：准备两个队列，queue1和queue2，元素入栈时，直接都入队queue1，
# 要出栈时，把queue1中除了最后一个元素之外的其它元素全部出队，
# 然后按照出队的顺序依次入queue2，将此时queue1中的唯一剩余元素作为栈顶出队，这就是要出栈的元素
# 接下来如果再有元素入栈，则全部入队queue2，此时的queue2就充当了之前queue1的角色
# 这样，两个栈总有一个是空的
from queue import Queue
class Stack():
    queue1=Queue()
    queue2=Queue()
    def inQueue(self,element):
        if self.queue1:
            self.queue1.put(element)
        else:# queue2不为空
            self.queue2.put(element)
    def popQueue(self):
        if  self.queue1.empty() and self.queue2.empty():
            print('空')
            return
        if not self.queue1.empty():
            while len(self.queue1.queue)>1:
                self.queue2.put(self.queue1.get())
            return self.queue1.get()
        else:# queue2不为空
            while len(self.queue2.queue)>1:
                self.queue1.put(self.queue2.get())
            return self.queue2.get()
stack=Stack()
print('入栈1，2，3')
stack.inQueue(1)
stack.inQueue(2)
stack.inQueue(3)
print(stack.queue1.queue,stack.queue2.queue)#deque([1, 2, 3]) deque([])
stack.popQueue()
print('出栈')
print(stack.queue1.queue,stack.queue2.queue)
stack.popQueue()
print('出栈')
print(stack.queue1.queue,stack.queue2.queue)
print('入栈4，5')
print(stack.queue1.queue,stack.queue2.queue)
stack.inQueue(4)
stack.inQueue(5)
print(stack.queue1.queue,stack.queue2.queue)
print('出栈')
stack.popQueue()
print(list(stack.queue1.queue),list(stack.queue2.queue))

    