class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = 0
        while(left <= right):
            t = 0
            mid = (left + right) // 2
            for i in piles:
                t += (i + mid - 1) // mid
            if t <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
