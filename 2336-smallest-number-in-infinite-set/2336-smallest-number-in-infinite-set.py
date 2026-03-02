import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.cur = 1
        heapq.heappush(self.heap, self.cur)

    def popSmallest(self) -> int:
        t = heapq.heappop(self.heap)
        if t == self.cur:
            self.cur += 1
            heapq.heappush(self.heap, self.cur)
        return t

    def addBack(self, num: int) -> None:
        if num < self.cur and num not in self.heap:
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)