#Design a stack that supports push, pop, top, and retrieving the minimum element
#in constant time.
#
#push(x) -- Push element x onto stack.
#pop() -- Removes the element on top of the stack.
#top() -- Get the top element.
#getMin() -- Retrieve the minimum element in the stack.
# 
#
#Example 1:
#
#Input
#["MinStack","push","push","push","getMin","pop","top","getMin"]
#[[],[-2],[0],[-3],[],[],[],[]]

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        tupl = [x, min(x, self.stack[-1][1])]
        self.stack.append(tupl)
        return None

    def pop(self) -> None:
        if len(self.stack) != 0:
            return self.stack.pop()[0]
        else:
            return None

    def top(self) -> int:
        if len(self.stack) == 0:
            return 0
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return 0        
        return self.top()[1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(1)
# obj.pop(2)
# param_3 = obj.top()
# param_4 = obj.getMin()
