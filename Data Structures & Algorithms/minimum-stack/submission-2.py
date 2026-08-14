class MinStack:

    def __init__(self):
        self.s = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.minstack:
            self.minstack.append(min(val, self.minstack[-1]))
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.s:
            self.s.pop()
            self.minstack.pop()

    def top(self) -> int:
        if self.s:
            return self.s[-1]
        return 0  # or raise IndexError("Stack is empty")

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        return 0  # or raise IndexError("Stack is empty")
