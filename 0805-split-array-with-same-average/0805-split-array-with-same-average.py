class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        m = n // 2
        total = sum(nums)
        if not any(total * k % n == 0 for k in range(1, m + 1)):
            return False

        sums = [set() for _ in range(m + 1)]
        sums[0].add(0)
        for num in nums:
            for i in range(m, 0, -1):
                for prev in sums[i - 1]:
                    sums[i].add(prev + num)

        for k in range(1, m + 1):
            if total * k % n == 0 and (total * k // n) in sums[k]:
                return True
        return False