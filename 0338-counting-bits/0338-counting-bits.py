class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range (n+1):
            t = 0
            j = i
            while j > 0:
                if j % 2:
                    t += 1
                j //= 2
            ans.append(t)
        return ans