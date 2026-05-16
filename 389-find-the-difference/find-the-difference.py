class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = Counter(s)
        for char in t:
            if hashmap[char] <= 0:
                return char
            hashmap[char] -= 1
        