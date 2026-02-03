from collections import deque

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k-1
        m = t = sum(nums[:k])
        while (r < len(nums)-1):
            t -= nums[l]
            l += 1
            r += 1
            t += nums[r]
            if t > m:
                m = t
        return m / k