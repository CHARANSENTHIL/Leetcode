class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2 or x % 2 == 0: return x == 2
            return all(x % d != 0 for d in range(3, int(x**0.5) + 1, 2))

        if 8 <= n <= 11:
            return 11
        for l in range(1, 6):
            for root in range(10**(l - 1), 10**l):
                s = str(root)
                p = int(s + s[-2::-1])
                if p >= n and is_prime(p):
                    return p
        return -1