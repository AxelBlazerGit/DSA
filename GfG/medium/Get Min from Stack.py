class Solution:

    def __init__(self):
        # code here
        self.stk = []
        self.minn = None
        
    # Add an element to the top of Stack
    def push(self, x):
        # code here
        if not self.stk:
            self.stk.append(x)
            self.minn = x
        elif x >= self.minn:
            self.stk.append(x)
        else:
            self.stk.append(2 * x - self.minn)
            self.minn = x

    # Remove the top element from the Stack
    def pop(self):
        # code here
        if not self.stk:
            return -1
        top = self.stk.pop()
        if top < self.minn:
            prev = self.minn
            self.minn = 2 * self.minn - top
            return prev
        return top

    # Returns top element of Stack
    def peek(self):
        # code here
        if not self.stk:
            return -1
        return self.minn if self.stk[-1] < self.minn else self.stk[-1]

    # Finds minimum element of Stack
    def getMin(self):
        # code here
        return self.minn if self.stk else -1
