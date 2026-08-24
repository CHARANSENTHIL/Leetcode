class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = set(dictionary)
        tokens = sentence.split()
        n = len(tokens)

        for i in range(0, n):
            n_token = len(tokens[i])
            for j in range(1, n_token + 1):
                if tokens[i][:j] in root:
                    tokens[i] = tokens[i][:j]
                    break

        return " ".join(tokens)