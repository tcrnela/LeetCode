class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        vis = set()
        out = []
        s = 0
        ans = []

        def bt(s, out, p):
            if len(out) == k and s == n:
                    ans.append(out[:])
            
            for i in range (p, 10):
                if i not in vis:
                    s += i
                    vis.add(i)
                    out.append(i)
                    bt(s, out, i)
                    s -= i
                    vis.remove(i)
                    out.pop()

        bt(s, out, 1)
        return ans