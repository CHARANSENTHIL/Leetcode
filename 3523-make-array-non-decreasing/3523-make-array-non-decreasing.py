class Solution:
    def maximumPossibleSize(self, nums):
        prev, size = -1, 0; [((prev := num), (size := size + 1)) for num in nums if num >= prev]; return size