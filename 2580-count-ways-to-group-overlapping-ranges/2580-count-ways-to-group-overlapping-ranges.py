class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
           
        cnt, hi = 1, -1
        for a, b in sorted(ranges):
            if hi < a:
                cnt <<= 1
                cnt %= 10 ** 9 + 7
            hi = max(hi, b)
        return cnt