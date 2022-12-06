class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = deque()

    def next(self, val: int) -> float:
        current = len(self.window)
        while current >= self.size:
            self.window.popleft()
            current -= 1
        self.window.append(val)
        current += 1
        return sum(self.window)/current



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
