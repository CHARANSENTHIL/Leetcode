class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums1.extend(nums2)
        nums1 = sorted(nums1)
        n = len(nums1)//2
        if len(nums1)%2 == 0:
            x = nums1[n-1]+nums1[n]
            return x /2
        return nums1[n]

        