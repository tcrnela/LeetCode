class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        a = nums1 - nums2
        b = nums2 - nums1
        return [list(a), list(b)]