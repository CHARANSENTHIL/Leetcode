import itertools


class Solution:
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        A, B = map(set, zip(*paths))
        return (B-A).pop()