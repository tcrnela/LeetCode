class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for i in spells:
            l = 0
            r = len(potions)-1
            p = -1
            
            while(l <= r):
                mid = (l + r) // 2
                if potions[mid] * i >= success:
                    p = mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            if p == -1:
                ans.append(0)
            else:
                ans.append(len(potions) - p)

        return ans