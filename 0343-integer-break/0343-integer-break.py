class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def maxProduct(k):
            if memo[k] != -1:
                return memo[k]
            if k == 1:
                return 1
            result = -float('inf')
            for i in range(1, k):
                result = max(result, i * maxProduct(k - i), i * (k - i))
            memo[k] = result
            return result
        return maxProduct(n)