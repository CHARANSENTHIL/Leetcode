class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        candidates = list(words)
        for _ in range(30):
            if not candidates:
                break
            guess_word = min(candidates, key=lambda w1: max(sum(match(w1, w2) == d for w2 in candidates) for d in range(7)))
            matches = master.guess(guess_word)
            if matches == 6:
                return
            candidates = [w for w in candidates if match(guess_word, w) == matches]