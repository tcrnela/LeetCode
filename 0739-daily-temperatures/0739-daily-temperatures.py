class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        temperatures = list(enumerate(temperatures))
        stk = []
        for t in temperatures:
            while(stk and t[1] > stk[-1][1]):
                k = stk.pop()
                ans[k[0]] = t[0] - k[0]
            stk.append(t)
        return ans