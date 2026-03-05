from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        ans = 0

        for i in grid:
            d[tuple(i)] += 1
        for i in range (len(grid)):
            t = []
            for j in range (len(grid)):
                t.append(grid[j][i])
            ans += d[tuple(t)] 

        return ans
