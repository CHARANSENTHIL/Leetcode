class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(1, len(timeSeries)):
            ans += min(duration, timeSeries[i] - timeSeries[i-1])

        return ans + duration

        
        