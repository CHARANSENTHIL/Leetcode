import random

class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}

    def flip(self) -> List[int]:
        self.total -= 1
        r = random.randint(0, self.total)
        idx = self.map.get(r, r)
        self.map[r] = self.map.get(self.total, self.total)
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        self.map.clear()
        self.total = self.m * self.n