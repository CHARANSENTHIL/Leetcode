class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        candidates = {10**(l - 1) - 1, 10**l + 1}
        prefix = int(n[:(l + 1) // 2])
        for p in (prefix - 1, prefix, prefix + 1):
            s = str(p)
            candidates.add(int(s + s[-2 if l % 2 else -1::-1]))
        orig = int(n)
        candidates.discard(orig)
        return str(min(candidates, key=lambda x: (abs(x - orig), x)))