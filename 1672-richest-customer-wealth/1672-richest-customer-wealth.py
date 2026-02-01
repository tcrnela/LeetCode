class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        t = 0
        for i in range (len(accounts)):
            a = sum(accounts[i])
            if t < a:
                t = a
        return t