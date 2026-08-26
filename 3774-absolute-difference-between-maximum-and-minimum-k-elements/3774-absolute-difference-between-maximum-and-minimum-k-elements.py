class Solution:
    def absDifference(self, arr: list[int], k: int) -> int:
        arr.sort()
        smallSum = sum(arr[:k])      # smallest k
        largeSum = sum(arr[-k:])     # largest k
        return abs(largeSum - smallSum)