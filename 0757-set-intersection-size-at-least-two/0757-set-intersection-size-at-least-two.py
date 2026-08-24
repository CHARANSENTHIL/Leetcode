class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: [x[0], -x[1]])
        stk = deque([intervals[-1][0], intervals[-1][0] + 1])
        res = 2
        for i in range(len(intervals) - 2, -1, -1):
            r, l = intervals[i][0], intervals[i][1]
            if not r <= stk[-1] <= l:
                stk.pop()
                stk.appendleft(r)
                res += 1
            if not r <= stk[-1] <= l:
                stk.pop()
                stk.append(r + 1)
                res += 1
        return res