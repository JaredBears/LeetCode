from collections import defaultdict
class Logger:

    def __init__(self):
        self.log = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        allowed = self.log[message]
        if timestamp >= allowed:
            self.log[message] = timestamp + 10
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)