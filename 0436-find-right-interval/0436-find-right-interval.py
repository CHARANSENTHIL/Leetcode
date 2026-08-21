class WaveletNode:
    __slots__ = ['min_start_val', 'max_start_val', 'index', 'left', 'right']
    def __init__(self):
        # The tight spectral bounds tracking coordinates in this sub-resolution
        self.min_start_val = float('inf')
        self.max_start_val = float('-inf')
        # Stores the original interval index (only at the leaf level)
        self.index = -1
        self.left = None
        self.right = None

class SparseWaveletRouter:
    def __init__(self, domain_min: int, domain_max: int):
        self.root = WaveletNode()
        self.DOMAIN_MIN = domain_min
        self.DOMAIN_MAX = domain_max

    def inject_start_point(self, node: WaveletNode, start: int, end: int, coord: int, original_idx: int):
        """
        Injects an interval's start coordinate and its array index into the dyadic domain.
        """
        node.min_start_val = min(node.min_start_val, coord)
        node.max_start_val = max(node.max_start_val, coord)
        
        if start == end:
            node.index = original_idx
            return

        mid = (start + end) // 2
        if coord <= mid:
            if node.left is None:
                node.left = WaveletNode()
            self.inject_start_point(node.left, start, mid, coord, original_idx)
        else:
            if node.right is None:
                node.right = WaveletNode()
            self.inject_start_point(node.right, mid + 1, end, coord, original_idx)

    def route_nearest_right(self, node: WaveletNode, start: int, end: int, target_end: int) -> int:
        """
        Traverses the multi-scale bands to locate the smallest start point >= target_end.
        """
        # Fast Global Pruning: If this entire dyadic chunk contains no coordinates 
        # reaching the required threshold, skip searching it completely.
        if node is None or node.max_start_val < target_end:
            return -1

        if start == end:
            return node.index if node.min_start_val >= target_end else -1

        mid = (start + end) // 2
        
        # 1. Route Left: Search the left band first if target_end sits below mid,
        # and the left band possesses a maximum value high enough to satisfy the query.
        if target_end <= mid and node.left is not None and node.left.max_start_val >= target_end:
            left_res = self.route_nearest_right(node.left, start, mid, target_end)
            if left_res != -1:
                return left_res
                
        # 2. Route Right: Fallback or route directly to the right child if the left child 
        # is out of range or fails to produce a valid index.
        if node.right is not None and node.right.max_start_val >= target_end:
            return self.route_nearest_right(node.right, mid + 1, end, target_end)

        return -1


class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        if not intervals:
            return []
            
        min_bound = min(x[0] for x in intervals)
        max_bound = max(x[0] for x in intervals)
        
        if min_bound == max_bound:
            max_bound += 1
            
        router = SparseWaveletRouter(min_bound, max_bound)
        
        for idx, (start_i, _) in enumerate(intervals):
            router.inject_start_point(router.root, router.DOMAIN_MIN, router.DOMAIN_MAX, start_i, idx)
            
        result = []
        for _, end_i in intervals:
            ans_idx = router.route_nearest_right(router.root, router.DOMAIN_MIN, router.DOMAIN_MAX, end_i)
            result.append(ans_idx)
            
        return result