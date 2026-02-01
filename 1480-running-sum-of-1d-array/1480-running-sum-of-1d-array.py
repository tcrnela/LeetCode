class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = [0] * len(nums)
        s[0] = nums[0]
        for i in range (1, len(nums)):
            s[i] += s[i-1] + nums[i]
        return s