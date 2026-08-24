import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        sorted_nums = []
        
        # Process from right to left ⬅️
        for num in reversed(nums):
            # Find insertion position using binary search 🔍
            insert_pos = bisect.bisect_left(sorted_nums, num)
            result.append(insert_pos)
            # Insert into the sorted list to maintain order
            bisect.insort(sorted_nums, num)
        
        # Reverse to get the correct order 🔄
        return result[::-1]