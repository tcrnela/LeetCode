class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        a = 0
        ans = 0 
        zero = 0
        for b in range (len(nums)):
            if nums[b] == 0:
                zero += 1
            while (zero > k):
                if nums[a] == 0:
                    zero -= 1
                a += 1

            ans = max(ans, b-a+1)
        return ans
