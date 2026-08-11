class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        needed = Counter("balloon")
        return min(count[c] // needed[c] for c in needed)
        