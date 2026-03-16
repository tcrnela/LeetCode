class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 0
        left = 0
        right = len(nums)-1
        while (1):
            mid = (left + right) // 2
            if (mid == 0 and nums[mid] > nums[mid+1] or mid == len(nums)-1 and nums[mid] > nums[mid-1]):
                return mid
            if (nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]):
                return mid
            
            elif (nums[mid] > nums[mid+1]):
                right = mid - 1
            elif (nums[mid] < nums[mid+1]):
                left = mid + 1