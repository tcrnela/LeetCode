class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = cost + [0]
        dp = [float("inf")] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range (2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return dp[len(cost)-1]