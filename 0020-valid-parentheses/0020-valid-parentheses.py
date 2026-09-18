class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'}': '{', ']': '[', ')': '('}
        stack = []
        for ch in s:
            if ch in mp.values():
                stack.append(ch)
            elif not stack  or mp[ch] != stack.pop():
                return False
        return not stack