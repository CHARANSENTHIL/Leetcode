class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        from collections import Counter

        freq = Counter(nums)
        mn, mx = nums[0], nums[-1]

        a = b = c = 0

        for i in range(mn, mx + 2):
            f = freq[i]
            if f < a + b:
                return False
            old = a
            a = max(0, f - a - b - c)
            b = old
            c = f - a - b

        return True