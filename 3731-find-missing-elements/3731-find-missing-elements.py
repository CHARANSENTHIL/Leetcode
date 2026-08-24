class Solution:
    def findMissingElements(self, a: List[int]) -> List[int]:
        return sorted({*range(min(a),max(a)+1)}-{*a})