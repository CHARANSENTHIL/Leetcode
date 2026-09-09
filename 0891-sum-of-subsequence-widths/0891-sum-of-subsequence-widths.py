class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        ans = 0
        pow2 = 1
        n = len(nums)
        for i in range(n):
            ans = (ans + (nums[i] - nums[n - 1 - i]) * pow2) % MOD
            pow2 = (pow2 * 2) % MOD
        return ans