class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        used = 0
        l = 0
        for r in range (len(nums)):
            if nums[r] == 0 and used == 0:
                used = 1
            elif nums[r] == 0 and used == 1:
                while (nums[l] == 1):
                    l += 1
                l += 1
            if r-l+1 > ans:
                ans = r-l+1
        return ans-1