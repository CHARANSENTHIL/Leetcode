class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:

        n, ptr = len(nums), 0

        for num in nums:                # Write zeros
            if num%2 == 0:
                nums[ptr] = 0
                ptr+= 1

        for i in range(ptr, n):         # Fill in remainder
            nums[i] = 1                 # of nums with ones

        return nums    