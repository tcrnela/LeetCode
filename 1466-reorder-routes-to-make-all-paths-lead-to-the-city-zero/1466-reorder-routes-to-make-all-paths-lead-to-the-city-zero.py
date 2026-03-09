from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        grp = defaultdict(list)
        for a, b in connections:
            grp[a].append((b, 1))
            grp[b].append((a, 0))
        ans = 0 
        vis = {0}
        stk = [0]

        while stk:
            cur = stk.pop()
            for a, b in grp[cur]:
                if a not in vis:
                    vis.add(a)
                    ans += b
                    stk.append(a)
        return ans