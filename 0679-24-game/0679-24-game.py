class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return abs(cards[0] - 24) < 1e-6
        for i in range(len(cards)):
            for j in range(len(cards)):
                if i != j:
                    next_cards = [cards[k] for k in range(len(cards)) if k != i and k != j]
                    p, q = float(cards[i]), float(cards[j])
                    for val in (p + q, p - q, q - p, p * q, p / q if q else None, q / p if p else None):
                        if val is not None and self.judgePoint24(next_cards + [val]):
                            return True
        return False