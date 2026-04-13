class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            return None
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]


if __name__ == "__main__":
    obj = MinStack()

    obj.push(5)
    obj.push(2)
    obj.push(10)
    obj.push(1)

    print(obj.top())
    print(obj.getMin())

    obj.pop()

    print(obj.top())
    print(obj.getMin())

    obj.pop()

    print(obj.top())
    print(obj.getMin())
