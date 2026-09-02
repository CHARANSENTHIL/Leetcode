class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack and stack[-1] == num:
                num += stack.pop()
            stack.append(num)

        return stack