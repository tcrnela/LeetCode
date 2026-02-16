from itertools import accumulate

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = list(accumulate(nums))
        s = [0] + s + [0]
        for i in range(1, len(s)-1):
            if s[i-1] == s[len(s)-2] - s[i]:
                return i-1
        return -1