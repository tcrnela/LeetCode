class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = [0] * n
        b = [0] * n
        a[0] = nums[0]
        b[-1] = nums[-1]
        ans = []

        for i in range (1, n):
            a[i] = a[i-1] * nums[i]
        for i in range (n-2, -1, -1):
            b[i] = b[i+1] * nums[i]
        a = [1] + a + [1]
        b = [1] + b + [1]
        for i in range (1, n+1):
            ans.append(a[i-1] * b[i+1])
        return ans