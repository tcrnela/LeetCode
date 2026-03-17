class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        vol = 1
        while(self.stk and price >= self.stk[-1][0]):
            vol += self.stk.pop()[1]
        self.stk.append((price, vol))

        return vol

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)