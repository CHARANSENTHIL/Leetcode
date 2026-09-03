class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}
        for i, d in enumerate(digits):
            for d_larger in range(9, int(d), -1):
                if last.get(d_larger, -1) > i:
                    digits[i], digits[last[d_larger]] = digits[last[d_larger]], digits[i]
                    return int("".join(digits))
        return num