class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        t = max(candies)
        a = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= t:
                a[i] = True
        return a
