class MinStack:
    def __init__(self):
        self.stack: list[int] = []
        self.minimums: list[list[int, int]] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimums:
            m = self.getMin()
            if val < m:
                self.minimums.append([val, 1])
            elif val == m:
                self.minimums[-1][1] += 1
        else:
            self.minimums.append([val, 1])

    def pop(self) -> None:
        res = self.stack.pop()

        m = self.getMin()
        if res == m:
            self.minimums[-1][1] -= 1
            if self.minimums[-1][1] == 0:
                self.minimums.pop()

        return res

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1][0]
