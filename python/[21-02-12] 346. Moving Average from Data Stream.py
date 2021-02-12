"""
[21-01-04] 346. Moving Average from Data Stream
https://leetcode.com/problems/moving-average-from-data-stream/
"""

class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = []
        self.tot = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.tot += val
        if len(self.queue)>self.size:
            temp = self.queue.pop(0)
            self.tot -= temp
        return self.tot / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
